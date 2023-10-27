from django.db import transaction
from django.db.models import Model, QuerySet
from djoser.serializers import UserCreateSerializer
from drf_spectacular.utils import extend_schema_field
from rest_framework.serializers import (
    DictField, IntegerField, ListField,
    ModelSerializer, SerializerMethodField,
    ValidationError,
)

from user.models import HrTask, User
from vacancy.models import (
    City, Currency, Employment, Experience, Language, LanguageLevel,
    Skill, SkillCategory, Vacancy, VacancyLanguage, VacancySkill,
)


class CitySerializer(ModelSerializer):
    """Сериализатор представления городов."""

    class Meta:
        model = City
        fields = (
            'id',
            'name',
        )


class CurrencySerializer(ModelSerializer):
    """Сериализатор представления валюты."""

    class Meta:
        model = Currency
        fields = (
            'id',
            'name',
            'symbol',
        )


class EmploymentSerializer(ModelSerializer):
    """Сериализатор представления форматов работы."""

    class Meta:
        model = Employment
        fields = (
            'id',
            'name',
        )


class ExperienceSerializer(ModelSerializer):
    """Сериализатор представления сроков опыта работы."""

    class Meta:
        model = Experience
        fields = (
            'id',
            'name',
        )


class LanguageSerializer(ModelSerializer):
    """Сериализатор представления разговорных языков."""

    class Meta:
        model = Language
        fields = (
            'id',
            'name',
        )


class ScheduleSerializer(ModelSerializer):
    """Сериализатор представления графиков работы."""

    class Meta:
        model = Language
        fields = (
            'id',
            'name',
        )


class SkillSerializer(ModelSerializer):
    """Сериализатор представления навыков."""

    class Meta:
        model = Skill
        fields = (
            'id',
            'name',
        )


class SkillCategorySerializer(ModelSerializer):
    """Сериализатор представления навыков, сгруппированных по категориям."""

    skills = SerializerMethodField()

    class Meta:
        model = SkillCategory
        fields = ('name', 'skills',)

    @extend_schema_field(ListField(child=SkillSerializer()))
    def get_skills(self, obj):
        skill_serializer: SkillSerializer = SkillSerializer(
            instance=obj.skill.all(),
            many=True
        )
        return skill_serializer.data


class TaskSerializer(ModelSerializer):
    """Сериализатор представления задач HR-специалиста."""

    class Meta:
        model = HrTask
        fields = (
            'id',
            'hr',
            'description',
            'date',
            'time',
        )

    def to_representation(self, instance):
        # INFO: при передачи query параметра формата YYYY-DD сериализатор
        #       должен вернуть не объекты queryset, а список list[int] дней
        #       календаря, в которых есть хотя бы одна задача.
        if isinstance(instance, int):
            return instance
        data: dict[str, str] = super().to_representation(instance)
        data.pop('hr')
        return data


class UserRegisterSerializer(UserCreateSerializer):
    """Сериализатор для создания нового HR-специалиста."""

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'phone',
        )


class UserUpdateSerializer(ModelSerializer):
    """Сериализатор представления HR-специалиста."""

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone',
            'avatar',
            'date_joined',
        )


class VacancySerializer(ModelSerializer):
    """Сериализатор представления вакансий."""

    languages = ListField(
        child=DictField(child=IntegerField()),
        write_only=True,
    )
    skills = ListField(child=IntegerField(), write_only=True)

    class Meta:
        model = Vacancy
        fields = (
            'id',
            'hr',
            'name',
            'city',
            'address',
            'description',
            'responsibilities',
            'conditions',
            'salary_from',
            'salary_to',
            'currency',
            'testcase',
            'experience',
            'employment',
            'schedule',
            'skills',
            'languages',
            'pub_datetime',
            'is_archived',
            'is_template',
        )
        read_only_fields = ('id', 'hr',)

    def validate_languages(self, value):
        """
        Производит валидацию поля "languages".
        Возвращает Queryset моделей Language и LanguageLevel.
        """
        languages_ids: dict[int, True] = {}
        levels_ids: list[int] = []
        for language in value:
            languages_ids[language.get('language')] = True
            levels_ids.append(language.get('level'))
        if len(languages_ids) != len(value):
            raise ValidationError(
                {"Bad Request.": "Один и тот же язык указан дважды."}
            )
        languages: QuerySet = self._validate_ids(
            ids=list(languages_ids),
            model=Language,
            desc='разговорных языков'
        )
        levels: QuerySet = self._validate_ids(
            ids=list(set(levels_ids)),
            model=LanguageLevel,
            desc='уровней владения языком'
        )
        return languages, levels, value

    def validate_skills(self, value):
        return self._validate_ids(
            ids=value, model=Skill, desc='навыков'
        )

    def validate(self, attrs):
        name: str = attrs.get('name')
        description: str = attrs.get('description')
        if Vacancy.objects.filter(name=name, description=description).exists():
            raise ValidationError(
                {"Bad Request.": "Такая вакансия уже существует."}
            )
        return super().validate(attrs)

    @transaction.atomic
    def create(self, validated_data):
        validated_data['hr'] = self.context['request'].user
        language_qs, levels_qs, lang_data = validated_data.pop('languages')
        skills: QuerySet = validated_data.pop('skills')
        instance: Vacancy = super().create(validated_data)
        instance.experience = validated_data.get('experience')
        instance.save()
        self._create_vacancy_languages(
                language_data=lang_data,
                vacancy=instance,
                language_qs=language_qs,
                levels_qs=levels_qs,
            )
        self._create_vacancy_skills(vacancy=instance, skills=skills)
        return instance

    def to_representation(self, instance):
        data: dict[str, any] = super().to_representation(instance)
        vacancy_languages: QuerySet = instance.vacancy_language.all()
        data['languages'] = [
            {'language': language.language.name, 'level': language.level.name}
            for language in vacancy_languages
        ]
        vacancy_skills: QuerySet = instance.vacancy_skill.all()
        data['skills'] = [
            {'name': vacancy_skill.skill.name}
            for vacancy_skill in vacancy_skills
        ]
        data['city'] = instance.city.name
        data['currency'] = instance.currency.name
        data['experience'] = instance.experience.name
        data['employment'] = {"name": instance.employment.name}
        data['schedule'] = {"name": instance.schedule.name}
        return data

    def _create_vacancy_languages(
                self,
                language_data: list[dict],
                vacancy: Vacancy,
                language_qs: QuerySet,
                levels_qs: QuerySet
            ) -> None:
        """Создает объекты модели VacancyLanguage."""
        vacancy_languages: list[VacancyLanguage] = []
        for data in language_data:
            vacancy_languages.append(
                VacancyLanguage(
                    vacancy=vacancy,
                    language=language_qs.get(id=data.get('language')),
                    level=levels_qs.get(id=data.get('level'))
                )
            )
        VacancyLanguage.objects.bulk_create(vacancy_languages)
        return

    def _create_vacancy_skills(
                self, skills: QuerySet, vacancy: Vacancy
            ) -> None:
        """Создает объекты модели VacancySkill."""
        vacancy_skills: list[VacancySkill] = []
        for skill in skills:
            vacancy_skills.append(VacancySkill(vacancy=vacancy, skill=skill))
        VacancySkill.objects.bulk_create(vacancy_skills)
        return

    def _validate_ids(
                self, ids: list[int], model: Model, desc: str
            ) -> QuerySet:
        """
        Проверяет, что для сообщенных ID существуют объекты.
        Возвращает Queryset объектов.
        """
        queryset: QuerySet = model.objects.filter(id__in=ids)
        # TODO: можно вывести список невалидных ID при необходимости.
        if queryset.count() != len(ids):
            raise ValidationError(
                {"Bad Request.": f"Некоторых указанных {desc} не существует."}
            )
        return queryset
