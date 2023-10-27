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
    EXPERIENCE_VIEW_SCHEMA, LANGUAGE_VIEW_SCHEMA, SCHEDULE_VIEW_SCHEMA,
    SKILL_CATEGORY_VIEW_SCHEMA, SKILL_SEARCH_VIEW_SCHEMA,
    TASK_VIEW_SCHEMA, TASK_VIEW_LIST_SCHEMA,
    TOKEN_OBTAIN_SCHEMA, TOKEN_REFRESH_SCHEMA,
    USER_VIEW_SCHEMA, USER_ME_SCHEMA,
    VACANCY_VIEW_SCHEMA,
)
from api.v1.permissions import IsOwnerPut
from api.v1.serializers import (
    CitySerializer, CurrencySerializer, EmploymentSerializer,
    ExperienceSerializer, LanguageSerializer, ScheduleSerializer,
    SkillSerializer, SkillCategorySerializer, TaskSerializer,
    VacancySerializer, UserRegisterSerializer, UserUpdateSerializer,
)
from user.models import (
    City, Experience, HrTask, Language, Skill, SkillCategory, User,
)
from vacancy.models import Currency, Employment, Schedule, Vacancy


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
@extend_schema_view(**VACANCY_VIEW_SCHEMA)
class VacancyViewSet(ModelViewSet):
    """Вью-сет для взаимодействия с моделью Vacancy."""

    http_method_names = ('get', 'post', 'patch',)
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.filter(
            hr=self.request.user,
        ).select_related(
            'hr',
            'city',
        ).prefetch_related(
            'vacancy_employment',
            'vacancy_skill',
            'vacancy_language',
        )

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
