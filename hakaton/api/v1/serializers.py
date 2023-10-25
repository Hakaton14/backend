from djoser.serializers import UserCreateSerializer
from rest_framework.serializers import ModelSerializer

from user.models import HrTasks, User


class TaskSerializer(ModelSerializer):
    """Сериализатор представления задач HR-специалиста."""

    class Meta:
        model = HrTasks
        fields = (
            'id',
            'hr',
            'description',
            'date',
            'time',
        )

    def to_representation(self, instance):
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
