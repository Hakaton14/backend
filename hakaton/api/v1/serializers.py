from django.db import transaction
from django.db.models import QuerySet
from djoser.serializers import UserCreateSerializer
from drf_spectacular.utils import extend_schema_field
from rest_framework.serializers import (
    IntegerField, ListField, ModelSerializer, SerializerMethodField,
    ValidationError,
)

from user.models import City, Experience, HrTask, Skill, SkillCategory, User
from vacancy.models import Currency, Vacancy, VacancySkill


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


class ExperienceSerializer(ModelSerializer):
    """Сериализатор представления сроков опыта работы."""

    class Meta:
        model = Experience
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
            'skills',
            'pub_datetime',
            'is_archived',
            'is_template',
        )

    def validate_skills(self, value):
        skills: QuerySet = Skill.objects.filter(id__in=value)
        # TODO: можно вывести список невалидных ID при необходимости.
        if skills.count() != len(value):
            raise ValidationError(
                {"Bad Request.": "Указанных навыков не существует."}
            )
        return skills

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
        skills: QuerySet = validated_data.pop('skills')
        instance: Vacancy = super().create(validated_data)
        instance.experience = validated_data.get('experience')
        instance.save()
        vacancy_skills: list[VacancySkill] = []
        for skill in skills:
            vacancy_skills.append(VacancySkill(vacancy=instance, skill=skill))
        VacancySkill.objects.bulk_create(vacancy_skills)
        return instance

    def to_representation(self, instance):
        data: dict[str, any] = super().to_representation(instance)
        vacancy_skills: QuerySet = instance.vacancy_skill.all()
        data['skills'] = [
            vacancy_skill.skill.name for vacancy_skill in vacancy_skills
        ]
        data['city'] = instance.city.name
        data['currency'] = instance.currency.name
        data['experience'] = instance.experience.name
        return data
