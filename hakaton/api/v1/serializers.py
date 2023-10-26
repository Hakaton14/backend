from django.db.models import QuerySet
from djoser.serializers import UserCreateSerializer
from drf_spectacular.utils import extend_schema_field
from rest_framework.serializers import (
    ListField, ModelSerializer, SerializerMethodField,
)

from user.models import HrTask, Skill, SkillCategory, User


class SkillSerializer(ModelSerializer):
    """Сериализатор представления навыков."""

    class Meta:
        model = Skill
        fields = ('id', 'name',)


class SkillCategorySerializer(ModelSerializer):
    """Сериализатор представления навыков, сгруппированных по категориям."""

    skills = SerializerMethodField()

    class Meta:
        model = SkillCategory
        fields = ('name', 'skills',)

    @extend_schema_field(ListField(child=SkillSerializer()))
    def get_skills(self, obj):
        skills: QuerySet = obj.skill.all()
        print(skills)
        skill_serializer: SkillSerializer = SkillSerializer(
            instance=skills,
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
        fields = fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'phone',
            'avatar',
            'date_joined',
        )
