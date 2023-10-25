from drf_spectacular.utils import extend_schema, OpenApiParameter

from api.v1.serializers import (
    TaskSerializer, UserRegisterSerializer, UserUpdateSerializer,
)

TASK_VIEW_SCHEMA: dict[str, str] = {
    'create': extend_schema(
        description='Создает новую задачу пользователя.',
        summary='Создать задачу пользователя.',
        request=TaskSerializer,
    ),
    'destroy': extend_schema(
        description=(
            'Удаляет задачу пользователя с указанным идентификатором.'
        ),
        summary='Удалить задачу пользователя.',
        request=TaskSerializer,
    ),
    'list': extend_schema(
        description=(
            'Возвращает список задач пользователя. '
            'При передачи необязательного query параметра date в формате '
            'YYYY-MM возвращает список задач за указанный месяц, '
            'в формате YYYY-MM-DD - за указанный день.'
        ),
        summary='Получить список задач пользователя.',
        request=TaskSerializer,
    ),
    'retrieve': extend_schema(
        description=(
            'Возвращает задачу пользователя с указанным идентификатором.'
        ),
        summary='Получить задачу пользователя.',
        request=TaskSerializer,
    ),
    'update': extend_schema(
        description=(
            'Обновляет задачу пользователя.'
        ),
        summary='Обновить задачу пользователя.',
        request=TaskSerializer,
    ),
}
TASK_VIEW_LIST_SCHEMA: dict[str, any] = {
    'parameters': [
        OpenApiParameter(
            name='date',
            location=OpenApiParameter.QUERY,
            description='Дата в формате YYYY-MM или YYYY-MM-DD.',
            required=False,
            type=str,
        ),
    ],
}

TOKEN_OBTAIN_SCHEMA: dict[str, str] = {
    'description': (
        'Принимает набор учетных данных пользователя и возвращает '
        'пару JWT-токенов доступа и обновления.'
    ),
    'summary': 'Получить пару JWT-токенов доступа и обновления.',
}

TOKEN_REFRESH_SCHEMA: dict[str, str] = {
    'description': (
        'Принимает JWT-токен обновления и возвращает JWT-токен доступа, '
        'если токен обновления действителен.'
    ),
    'summary': 'Обновить JWT-токен доступа.',
}

USER_VIEW_SCHEMA: dict[str, str] = {
    'create': extend_schema(
        description='Создает нового пользователя.',
        summary='Создать нового пользователя.',
        request=UserRegisterSerializer,
    ),
    'update': extend_schema(
        description='Обновляет пользователя с указанным идентификатором.',
        summary='Обновить пользователя.',
        request=UserUpdateSerializer,
    ),
}

USER_ME_SCHEMA: dict[str, str] = {
    'description': 'Возвращает авторизированного пользователя.',
    'summary': 'Получить авторизированного пользователя.',
}
