from djoser.serializers import UserCreateSerializer
from rest_framework.serializers import ModelSerializer

from user.models import HrTask, User


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
