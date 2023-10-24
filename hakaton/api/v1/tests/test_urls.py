import pytest

from api.v1.tests.fixtures import (
    client_auth_admin,
    API_TOKEN_CREATE_URL, API_TOKEN_REFRESH_URL,
    API_SCHEMA_URL, API_SWAGGER_URL,
    API_USERS_URL, API_USERS_ME_URL,
    CLIENT_METHODS, STATUS_NOT_ALLOWED, URL_MISSED_STATUSES,
)


@pytest.mark.django_db
class TestEndpointsAvailability():
    """
    Производит тест доступности эндпоинтов в urlpatterns.
    Тестируется именно доступность эндпоинтов, а не права доступа к ним.
    """

    @pytest.mark.parametrize(
            'url, meaning', [
                (API_TOKEN_CREATE_URL,
                 'получения JWT-токенов доступа и обновления'
                 ),
                (API_TOKEN_REFRESH_URL,
                 'обновления JWT-токена доступа'
                 ),
            ]
        )
    def test_auth_token(self, url, meaning) -> None:
        """Производит тест доступности эндпоинтов JWT."""
        response = client_auth_admin().post(url)
        assert response.status_code not in URL_MISSED_STATUSES, (
            f'Убедитесь, что эндпоинт {meaning} функционирует '
            f'и доступен по адресу "{url}".'
        )
        return

    @pytest.mark.parametrize(
            'url, meaning', [
                (API_SCHEMA_URL, 'схемы'),
                (API_SWAGGER_URL, 'Swagger представления'),
            ]
        )
    def test_schema(self, url, meaning) -> None:
        """Производит тест доступности эндпоинтов drf_spectacular."""
        response = client_auth_admin().get(url)
        assert response.status_code not in URL_MISSED_STATUSES, (
            f'Убедитесь, что эндпоинт получения {meaning} документации '
            f'функционирует и доступен по адресу "{url}".'
        )
        return

    @pytest.mark.parametrize(
            'method, url', [
                ('post', API_USERS_URL),
                ('put', f'{API_USERS_URL}1/'),
                ('get', API_USERS_ME_URL),
            ]
        )
    def test_user_viewset_available(self, method, url) -> None:
        """Производит тест доступности эндпоинтов UserViewSet."""
        method_function = CLIENT_METHODS.get(method)
        response = method_function(url)
        assert response.status_code not in URL_MISSED_STATUSES, (
            f'Убедитесь, что {method} запрос по адресу "{url}" доступен.'
        )
        return

    @pytest.mark.parametrize(
            'method, url', [
                ('get', API_USERS_URL),
                ('delete', f'{API_USERS_URL}1/'),
                ('patch', f'{API_USERS_URL}1/'),
                ('delete', API_USERS_ME_URL),
                ('post', API_USERS_ME_URL),
                ('patch', API_USERS_ME_URL),
            ]
        )
    def test_user_viewset_unavailable(self, method, url) -> None:
        """Производит тест доступности эндпоинтов UserViewSet."""
        method_function = CLIENT_METHODS.get(method)
        response = method_function(url)
        assert response.status_code == STATUS_NOT_ALLOWED, (
            f'Убедитесь, что {method} запрос по адресу "{url}" недоступен.'
        )
        return
