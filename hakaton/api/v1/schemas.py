from drf_spectacular.utils import extend_schema

from api.v1.serializers import UserRegisterSerializer, UserUpdateSerializer

TOKEN_OBTAIN_SCHEMA: dict[str, str] = {
    'description': (
        'Принимает набор учетных данных пользователя и возвращает '
        'пару JSON-токенов доступа и обновления.'
    ),
    'summary': 'Получить пару JSON-токенов доступа и обновления.',
}

TOKEN_REFRESH_SCHEMA: dict[str, str] = {
    'description': (
        'Принимает JSON-токен обновления и возвращает JSON-токен доступа, '
        'если токен обновления действителен.'
    ),
    'summary': 'Обновить JSON-токен доступа.',
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
