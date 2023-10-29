from django.db.models import Q, QuerySet
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)
from rest_framework.viewsets import ModelViewSet

from api.v1.filters import TaskMonthFilter
from api.v1.schemas import (
    CITY_VIEW_SCHEMA, CURRENCY_VIEW_SCHEMA, EMPLOYMENT_VIEW_SCHEMA,
    EXPERIENCE_VIEW_SCHEMA, LANGUAGE_VIEW_SCHEMA, LANGUAGE_LEVEL_VIEW_SCHEMA,
    SCHEDULE_VIEW_SCHEMA, SKILL_CATEGORY_VIEW_SCHEMA, SKILL_SEARCH_VIEW_SCHEMA,
    STUDENT_VIEW_SCHEMA, STUDENT_MARK_WATCHED_SCHEMA, TASK_VIEW_SCHEMA,
    TASK_VIEW_LIST_SCHEMA, TOKEN_OBTAIN_SCHEMA, TOKEN_REFRESH_SCHEMA,
    USER_VIEW_SCHEMA, USER_ME_SCHEMA,
    VACANCY_VIEW_SCHEMA,
)
from api.v1.permissions import IsOwnerPut
from api.v1.serializers import (
    CitySerializer, CurrencySerializer, EmploymentSerializer,
    ExperienceSerializer, LanguageSerializer, LanguageLevelSerializer,
    ScheduleSerializer, SkillSerializer, SkillCategorySerializer,
    StudentSerializer, TaskSerializer, VacancySerializer,
    UserRegisterSerializer, UserUpdateSerializer,
)
from student.models import Student
from user.models import HrTask, HrWatched, User
from vacancy.models import (
    City, Currency, Employment, Experience, Language, LanguageLevel,
    Schedule, Skill, SkillCategory, Vacancy,
)


@extend_schema(**CITY_VIEW_SCHEMA)
class CityView(ListAPIView):
    """
    Вью функция list предоставления городов.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        search_param: str = self.request.query_params.get('search')
        if search_param:
            return City.objects.filter(name__startswith=search_param)
        return City.objects.all()


@extend_schema(**EMPLOYMENT_VIEW_SCHEMA)
class EmploymentView(ListAPIView):
    """
    Вью функция list предоставления форматов работы.
    """
    queryset = Employment.objects.all()
    serializer_class = EmploymentSerializer


@extend_schema(**CURRENCY_VIEW_SCHEMA)
class CurrencyView(ListAPIView):
    """
    Вью функция list предоставления валюты.
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


@extend_schema(**EXPERIENCE_VIEW_SCHEMA)
class ExperienceView(ListAPIView):
    """
    Вью функция list предоставления сроков опыта работы.
    """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


@extend_schema(**LANGUAGE_VIEW_SCHEMA)
class LanguageView(ListAPIView):
    """
    Вью функция list предоставления разговорных языков.
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


@extend_schema(**LANGUAGE_LEVEL_VIEW_SCHEMA)
class LanguageLevelView(ListAPIView):
    """
    Вью функция list предоставления разговорных языков.
    """
    queryset = LanguageLevel.objects.all()
    serializer_class = LanguageLevelSerializer


@extend_schema(**SCHEDULE_VIEW_SCHEMA)
class ScheduleView(ListAPIView):
    """
    Вью функция list предоставления графиков работы.
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


@extend_schema(**SKILL_CATEGORY_VIEW_SCHEMA)
class SkillCategoryView(ListAPIView):
    """
    Вью функция list предоставления навыков, сгруппированных по категориям.
    """
    queryset = SkillCategory.objects.prefetch_related('skill').all()
    serializer_class = SkillCategorySerializer


@extend_schema(**SKILL_SEARCH_VIEW_SCHEMA)
class SkillSearchView(ListAPIView):
    """
    Вью функция list предоставления навыков.
    Позволяет использовать search параметр для фильтрации по названию.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        search_param: str = self.request.query_params.get('search')
        if search_param:
            return Skill.objects.filter(name__startswith=search_param)
        return Skill.objects.all()


@extend_schema_view(**STUDENT_VIEW_SCHEMA)
class StudentViewSet(ModelViewSet):
    """Вью-сет для взаимодействия с моделью Student."""
    # INFO: метод POST нужен для того, чтобы дочерние @action
    #       эндпоинты с методом POST были доступны.
    # TODO: выдавать список просмотренных.
    http_method_names = ('get', 'post',)
    serializer_class = StudentSerializer

    def get_queryset(self):
        students: QuerySet = Student.objects.all(
        ).select_related(
            'city',
            'experience',
        ).prefetch_related(
            'student_employment',
            'student_language',
            'student_schedule',
            'student_skill',
        )
        from_vacancy: QuerySet = self._get_from_vacancy(
            vacancy_id=self.request.query_params.get('from_vacancy'),
            students=students,
        )
        if from_vacancy:
            return from_vacancy
        from_query: QuerySet = self._get_from_query(
            students=students,
            query=self.request.query_params,
        )
        if from_query:
            return from_query
        return students

    @extend_schema(exclude=True)
    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    @extend_schema(**STUDENT_MARK_WATCHED_SCHEMA)
    # TODO: добавить возможность отмечать в просмотренное вакансии.
    @action(
        detail=True,
        methods=('post',),
        url_name='mark_watched',
    )
    def mark_watched(self, request, pk: int):
        candidate: Student = get_object_or_404(Student, id=pk)
        HrWatched.objects.create(
            hr=request.user,
            candidate=candidate
        )
        return Response(status=status.HTTP_200_OK)

    def _get_from_query(self, students: QuerySet, query: dict[str, any]) -> QuerySet:  # noqa (E501)
        """
        Проверяет query параметры. Если хотя бы один параметр существует,
        возвращает всех кандидатов, которые соответствуют.
        Иначе - возвращает None.
        """
        # TODO: подумать над рефакторингом и оптимизацией.
        if query.get('city') is not None:
            students: QuerySet = self._filter_by_city(
                students=students,
                city=City.objects.get(id=query.get('city'))
            )
        if query.get('experience') is not None:
            students: QuerySet = self._filter_by_experience(
                students=students,
                experience=Experience.objects.get(id=query.get('experience'))
            )
        if query.get('employment') is not None:
            students: QuerySet = self._filter_by_employment(
                students=students,
                employment=Employment.objects.get(id=query.get('employment'))
            )
        if query.get('schedule') is not None:
            students: QuerySet = self._filter_by_schedule(
                students=students,
                schedule=Schedule.objects.get(id=query.get('schedule'))
            )
        if query.get('skills') is not None:
            students: QuerySet = self._filter_by_skills(
                students=students,
                skill_ids=query.get('skills')
            )
        if query.get('languages') is not None:
            languages_data: list[str] = list(query.get('languages').split(','))
            languages: list[dict[str, int]] = []
            for language in languages_data:
                language_id, language_level = language.split('-')
                languages.append(
                    {
                        'language_id': language_id,
                        'language_level': language_level
                    }
                )
            students: QuerySet = self._filter_by_languages(
                students=students,
                languages=languages,
            )
        return students


    def _get_from_vacancy(self, vacancy_id: str, students: QuerySet) -> QuerySet:  # noqa (E501)
        """
        Проверяет query параметр 'from_vacancy'. Если такой параметр существует
        и является ID существующей вакансии - возвращает всех кандидатов,
        которые подходят под требования вакансии.
        Иначе - возвращает None.
        """
        try:
            vacancy_id: int = int(vacancy_id)
        except (TypeError, ValueError):
            vacancy_id: None = None
        if (vacancy_id is None or
                not Vacancy.objects.filter(id=vacancy_id).exists()
                ):  # noqa (E124)
            return None
        vacancy: Vacancy = Vacancy.objects.select_related(
            'city',
            'experience',
            'employment',
            'schedule',
        ).prefetch_related(
            'vacancy_employment',
            'vacancy_language',
            'vacancy_skill',
        ).get(
            id=vacancy_id,
        )
        students: QuerySet = self._filter_by_city(
            students=students,
            city=vacancy.city
        )
        students: QuerySet = self._filter_by_employment(
            students=students,
            employment=vacancy.employment
        )
        students: QuerySet = self._filter_by_experience(
            students=students,
            experience=vacancy.experience
        )
        students: QuerySet = self._filter_by_languages(
            students=students,
            languages=list(
                {
                    'language_id': languages.language.id,
                    'language_level': languages.level.level
                } for languages in vacancy.vacancy_language.all()
            )
        )
        students: QuerySet = self._filter_by_schedule(
            students=students,
            schedule=vacancy.schedule
        )
        students: QuerySet = self._filter_by_skills(
            students=students,
            skill_ids=list(skill.id for skill in vacancy.vacancy_skill.all())
        )
        return students

    def _filter_by_city(self, students: QuerySet, city: City) -> QuerySet:
        """
        Принимает список студентов. Производит фильтрацию тех из них,
        кто имеет возможность работать непосредственно в офисе.
        Возвращает отфильтрованный список студентов.
        """
        return students.filter(Q(city=city) | Q(relocation=True))

    def _filter_by_experience(
            self, students: QuerySet, experience: Experience) -> QuerySet:
        """
        Принимает список студентов. Производит фильтрацию тех из них,
        кто имеет указанный в вакансии опыт работы.
        Возвращает отфильтрованный список студентов.
        """
        return students.filter(experience=experience)

    def _filter_by_employment(
            self, students: QuerySet, employment: Employment) -> QuerySet:
        """
        Принимает список студентов. Производит фильтрацию тех из них,
        кто имеет указанный в вакансии тип занятости.
        Возвращает отфильтрованный список студентов.
        """
        return students.filter(student_employment__employment=employment)

    def _filter_by_languages(
            self, students: QuerySet, languages: list[dict]) -> QuerySet:
        """
        Принимает список студентов. Производит фильтрацию тех из них,
        кто имеет все (или более) указанные в вакансии навыки.
        Возвращает отфильтрованный список студентов.
        """
        user_lists = [
            students.filter(
                student_language__language_id=language['language_id'],
                student_language__level__gte=language['language_level'],
            ).values_list(
                'id', flat=True
            ) for language in languages
        ]
        common_users = set(user_lists[0])
        for user_list in user_lists[1:]:
            common_users &= set(user_list)
        return students.filter(id__in=common_users)

    def _filter_by_schedule(
            self, students: QuerySet, schedule: Schedule) -> QuerySet:
        """
        Принимает список студентов. Производит фильтрацию тех из них,
        кто имеет указанный в вакансии график работы.
        Возвращает отфильтрованный список студентов.
        """
        return students.filter(student_schedule__schedule=schedule)

    def _filter_by_skills(
            self, students: QuerySet, skill_ids: list[int]) -> QuerySet:
        """
        Принимает список студентов. Производит фильтрацию тех из них,
        кто имеет все (или более) указанные в вакансии навыки.
        Возвращает отфильтрованный список студентов.
        """
        user_lists = [
            students.filter(
                student_skill__skill_id=skill_id
            ).values_list(
                'id', flat=True
            ) for skill_id in skill_ids
        ]
        common_users = set(user_lists[0])
        for user_list in user_lists[1:]:
            common_users &= set(user_list)
        return students.filter(id__in=common_users)


@extend_schema_view(**TASK_VIEW_SCHEMA)
class TaskViewSet(ModelViewSet):
    """Вью-сет для взаимодействия с моделью HrTask."""

    filter_backends = (TaskMonthFilter,)
    filterset_fields = ('date',)
    http_method_names = ('delete', 'get', 'patch', 'post',)
    serializer_class = TaskSerializer
    queryset = HrTask.objects.all()

    def get_queryset(self):
        return HrTask.objects.filter(hr=self.request.user)

    def create(self, request, *args, **kwargs):
        self.request.data['hr'] = self.request.user.id
        return super().create(request, *args, **kwargs)

    @extend_schema(**TASK_VIEW_LIST_SCHEMA)
    def list(self, request, *args, **kwargs):
        return super().list(self, request)


@extend_schema(**TOKEN_OBTAIN_SCHEMA)
class TokenObtainPairView(TokenObtainPairView):
    """Вью-класс обновления получения пары JWT-токенов доступа и обновления."""

    pass


@extend_schema(**TOKEN_REFRESH_SCHEMA)
class TokenRefreshView(TokenRefreshView):
    """Вью-класс обновления JWT-токена доступа."""

    pass


@extend_schema_view(**USER_VIEW_SCHEMA)
class UserViewSet(ModelViewSet):
    """Вью-сет для взаимодействия с моделью User."""

    queryset = User.objects.all()
    http_method_names = ('get', 'post', 'put',)

    @extend_schema(exclude=True)
    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserRegisterSerializer
        return UserUpdateSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PUT':
            self.permission_classes = (IsOwnerPut,)
        return super().get_permissions()

    @extend_schema(**USER_ME_SCHEMA)
    @action(detail=False,
            methods=('get',),
            url_path='me',
            url_name='users-me',
            )
    def me(self, request):
        instance: User = request.user
        serializer = UserUpdateSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


# TODO: ввиду того, что skills указаны как write_only,
#       в документации на GET запросы это поле не показано.
# TODO: дописать метод update().
# INFO: при обновлении вакансии возможно имеет смысл очистить список
#       просмотренных кандидатов, так как условия могли измениться.
#       Только при изменении ключевых полей: навыки, условия работы.
@extend_schema_view(**VACANCY_VIEW_SCHEMA)
class VacancyViewSet(ModelViewSet):
    """Вью-сет для взаимодействия с моделью Vacancy."""

    http_method_names = ('get', 'post', 'patch',)
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

    def get_queryset(self):
        # TODO: проверить актуальность полей.
        return Vacancy.objects.filter(
            hr=self.request.user,
        ).select_related(
            'hr',
            'city',
        ).prefetch_related(
            'vacancy_employment',
            'vacancy_language',
            'vacancy_skill',
        )

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
