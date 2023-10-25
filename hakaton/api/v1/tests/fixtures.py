from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient

from user.models import User

API_V1_URL: str = '/api/v1/'

API_SCHEMA_URL: str = f'{API_V1_URL}schema/'
API_SWAGGER_URL: str = f'{API_SCHEMA_URL}swagger-ui/'

API_TASKS_URL: str = f'{API_V1_URL}tasks/'

API_TOKEN_URL: str = f'{API_V1_URL}auth/token/'
API_TOKEN_CREATE_URL: str = f'{API_TOKEN_URL}create/'
API_TOKEN_REFRESH_URL: str = f'{API_TOKEN_URL}refresh/'

API_USERS_URL: str = f'{API_V1_URL}users/'
API_USERS_ME_URL: str = f'{API_USERS_URL}me/'

CLIENT_METHODS = {
    'delete': lambda url: client_auth_admin().delete(url),
    'get': lambda url: client_auth_admin().get(url),
    'patch': lambda url: client_auth_admin().patch(url),
    'post': lambda url: client_auth_admin().post(url),
    'put': lambda url: client_auth_admin().put(url),
}

TASK_DATA_HR_INVALID: dict[str, str] = {
    "hr": None,
    "description": "Test 1",
    "date": "2023-12-01",
    "time": "12:21:01"
}

USER_DATA_VALID: dict[str, str] = {
    "email": "testuser@email.com",
    "password": "MyPass!1",
    "first_name": "Илона",
    "last_name": "Маск",
    "phone": "+7 911 111 22 13"
}


# INFO: список статусов, которые может вернуть сервер,
#       если эндпоинт не доступен по указанному адресу.
URL_MISSED_STATUSES: list = [
    status.HTTP_301_MOVED_PERMANENTLY,
    status.HTTP_302_FOUND,
    status.HTTP_303_SEE_OTHER,
    status.HTTP_307_TEMPORARY_REDIRECT,
    status.HTTP_308_PERMANENT_REDIRECT,
    status.HTTP_404_NOT_FOUND,
    status.HTTP_405_METHOD_NOT_ALLOWED,
    status.HTTP_408_REQUEST_TIMEOUT,
    status.HTTP_409_CONFLICT,
    status.HTTP_410_GONE,
]

STATUS_NOT_ALLOWED: status = status.HTTP_405_METHOD_NOT_ALLOWED


def client_anon() -> APIClient:
    """Возвращает объект анонимного клиента."""
    return APIClient()


def client_auth() -> APIClient:
    """
    Возвращает объект авторизированного клиента.
    Авторизация производится форсированная: без использования токенов.
    """
    auth_client = APIClient()
    auth_client.force_authenticate(user=None)
    return auth_client


def create_user_obj(num: int) -> User:
    """
    Создает и возвращает объект модели "User".
    Высокое быстродействие за счет отсутствия шифрования пароля.
    Тесты, которые требуют валидации поля "password" будут провалены!
    """
    return User.objects.create(
        email=f'test_user_email_{num}@email.com',
        first_name=f'test_user_first_name_{num}',
        last_name=f'test_user_last_name_{num}',
        password=f'test_user_password_{num}!PASS',
        phone=f'+7 911 111 22 3{num}',
    )


def create_admin_user_obj(email, password):
    """Создает и возвращает объект администратора модели "User"."""
    admin: User = User.objects.create_superuser(
        email=email,
        password=password
    )
    return admin


def client_auth_admin(num: int = 1, admin: User = None) -> APIClient:
    """
    Возвращает объект авторизированного клиента по JWT токену.
    """
    if admin is None:
        admin: User = create_admin_user_obj(
            email=f'admin{num}@email.com',
            password='admin'
        )
    client: APIClient = client_anon()
    refresh: str = RefreshToken.for_user(admin)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client
