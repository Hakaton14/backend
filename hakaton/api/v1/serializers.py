from djoser.serializers import UserCreateSerializer
from rest_framework.serializers import ModelSerializer

from user.models import User


class UserRegisterSerializer(UserCreateSerializer):
    """Сериализатор для создания нового HR-пользователя."""

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
    """Сериализатор представления HR пользователя."""

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
