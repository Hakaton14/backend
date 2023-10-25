import pytest

from api.v1.tests.fixtures import (
    client_anon, client_auth_admin, create_user_obj, create_admin_user_obj,
    API_TOKEN_CREATE_URL, API_TOKEN_REFRESH_URL,
    API_TASKS_URL, API_USERS_URL, API_USERS_ME_URL,
    TASK_DATA_HR_INVALID, USER_DATA_VALID,
)
from user.models import HrTask, User


@pytest.mark.django_db
class TestEndpoints():
    """
    Производит тест функционала эндпоинтов в urlpatterns.
    """

    def _get_jwt_tokens(self) -> dict[str, str]:
        """
        Отправляет POST запрос на получение
        пары JWT-токенов доступа и обновления.
        """
        user = create_user_obj(num=1)
        password_str: str = user.password
        user.set_password(user.password)
        user.save()
        response = client_anon().post(
            path=API_TOKEN_CREATE_URL,
            data={
                "email": user.email,
                "password": password_str
            },
            format='json',
        )
        return response

    def test_get_jwt_tokens(self) -> None:
        """
        Тест POST запроса на получение пары JWT-токенов доступа и обновления.
        """
        data: dict = self._get_jwt_tokens().data
        missed_tokens: list[str] = []
        for token in ('access', 'refresh'):
            if token not in data:
                missed_tokens.append(token)
        assert not missed_tokens, (
            f'Убедитесь, что эндпоинт {API_TOKEN_CREATE_URL} возвращает '
            f'токен(ы): {", ".join(token for token in missed_tokens)}'
        )
        return

    def test_refresh_jwt_token(self) -> None:
        """
        Тест POST запроса на обновление JWT-токена доступа.
        """
        data: dict = self._get_jwt_tokens().data
        refresh_token: str = data.get('refresh')
        old_access_token: str = data.get('access')
        response = client_anon().post(
            path=API_TOKEN_REFRESH_URL,
            data={
                "refresh": refresh_token
            },
            format='json',
        )
        assert 'access' in response.data, (
            f'Убедитесь, что эндпоинт {API_TOKEN_REFRESH_URL} '
            'возвращает токен доступа.'
        )
        assert response.data.get('access') != old_access_token, (
            f'Убедитесь, что эндпоинт {API_TOKEN_REFRESH_URL} '
            'возвращает новый токен доступа.'
        )

    def _compare_user_data(self, user_data: dict[str, str]) -> None:
        """
        Сверяет данные последнего созданного пользователя с user_data.
        """
        last_user: User = User.objects.latest('id')
        invalid_data: list[str] = []
        # INFO: пароль хранится в хешированном виде.
        user_data.pop('password')
        for field in user_data:
            if getattr(last_user, field) != user_data.get(field):
                invalid_data.append(field)
        assert not invalid_data, (
            'Убедитесь, что пользователь создается с теми данными, '
            'которые были сообщены. Неверные данны для полей: '
            f'{", ".join(token for token in invalid_data)}'
        )

    def test_tasks_post(self) -> None:
        """Тест POST запроса на создание новой задачи."""
        tasks_count: int = HrTask.objects.count()
        task_data_valid: dict[str, str] = TASK_DATA_HR_INVALID.copy()
        admin: User = create_admin_user_obj(
            email='admin@email.com',
            password='AdminPass!1',
        )
        client = client_auth_admin(
            num=1,
            admin=admin,
        )
        task_data_valid['hr'] = 1
        client.post(
            path=API_TASKS_URL,
            data=task_data_valid,
            format='json',
        )
        tasks_count_new: int = HrTask.objects.count()
        assert tasks_count + 1 == tasks_count_new, (
            f'Убедитесь, что POST запрос на {API_TASKS_URL} с валидными '
            'данными создает нового пользователя.'
        )
        last_task: HrTask = HrTask.objects.latest('id')
        assert last_task.description == task_data_valid.get('description')
        return

    def test_users_post(self) -> None:
        """Тест POST запроса на создание нового пользователя."""
        users_cont: int = User.objects.all().count()
        user_data_valid: dict[str, str] = USER_DATA_VALID.copy()
        client_anon().post(
            path=API_USERS_URL,
            data=user_data_valid,
            format='json',
        )
        users_cont_new: int = User.objects.all().count()
        assert users_cont + 1 == users_cont_new, (
            f'Убедитесь, что POST запрос на {API_USERS_URL} с валидными '
            'данными создает нового пользователя.'
        )
        self._compare_user_data(user_data=user_data_valid)
        return

    def test_users_put(self) -> None:
        """Тест PUT запроса на изменение пользователя."""
        user_data_valid: dict[str, str] = USER_DATA_VALID.copy()
        client_auth_admin().put(
            path=f'{API_USERS_URL}1/',
            data=user_data_valid,
            format='json',
        )
        self._compare_user_data(user_data=user_data_valid)
        return

    def test_users_me_get(self) -> None:
        """Тест GET запроса пользователя."""
        user_data: dict[str, str] = {
            "email": 'admin1@email.com',
            "password": 'admin'
        }
        client_auth_admin().get(API_USERS_ME_URL)
        self._compare_user_data(user_data=user_data)
        return
