from datetime import timedelta
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR: Path = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'), verbose=True)


"""Database settings."""


# INFO: пагинация объектов в Django Admin.
ADMIN_LIST_PER_PAGE: int = 15

CITIES_MAX_LEN: int = 30

CURRENCY_MAX_LEN: int = 30
CURRENCY_SYMBOL_MAX_LEN: int = 1

DB_ENGINE: str = os.getenv('DB_ENGINE')
DB_USER: str = os.getenv('POSTGRES_USER')
DB_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
DB_HOST: str = os.getenv('DB_HOST')
DB_PORT: str = os.getenv('DB_PORT')
DB_NAME: str = os.getenv('POSTGRES_DB')

DB_POSTGRESQL: dict[str, dict[str, str]] = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

DB_SQLITE: dict[str, dict[str, str]] = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DJANGO_HASH_LEN: int = 512

EMPLOYMENT_MAX_LEN: int = 30

EXP_MAX_LEN: int = 30

LANGUAGE_MAX_LEN: int = 30

LANGUAGE_LEVEL_MAX_LEN: int = 30

SCHEDULE_MAX_LEN: int = 30

SKILL_MAX_LEN: int = 50

STUDENT_ABOUT_MAX_LEN: int = 150
STUDENT_LINK_MAX_LEN: int = 50
STUDENT_SPEC_MAX_LEN: int = 30

TASK_DESCRIPTION_MAX_LEN: int = 50

VACANCY_CURR_MAX_LEN: int = 10
VACANCY_EXP_MAX_LEN: int = 10
VACANCY_NAME_MAX_LEN: int = 30
VACANCY_ADDRESS_MAX_LEN: int = 60
VACANCY_STUDENT_STATUS_MAX_LEN: int = 30
VACANCY_TEMPLATE_INVITE: str = 'Вы нам подходите! Ура!'
VACANCY_TEXT_MAX_LEN: int = 512

USER_NAME_MAX_LEN: int = 30

USER_PHOTO_FOLDER: str = 'user/avatar/'


def user_avatar_get_name(user_email: str) -> str:
    """
    Формирует на основании электронной почты пользователя уникальное
    наименование его аватара, заменяя '@' и '.' на '_'.
    Расширение приводится к '.jpg'.
    """
    return (
        f"{user_email.replace('@', '_').replace('.', '_')}.jpg"
    )


def user_avatar_path(instance, filename) -> str:
    """
    Присваивает загружаемому изображению-аватару
    путь с уникальным именем изобажения.
    """
    unique_filename: str = user_avatar_get_name(user_email=instance.email)
    return f'{USER_PHOTO_FOLDER}{unique_filename}'

"""Email settings."""


DEFAULT_FROM_EMAIL = 'Praktikum Services'

EMAIL_HOST: str = os.getenv('EMAIL_HOST')

EMAIL_PORT: int = int(os.getenv('EMAIL_PORT'))

EMAIL_HOST_USER: str = os.getenv('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD: str = os.getenv('EMAIL_HOST_PASSWORD')

EMAIL_USE_TLS: bool = bool(os.getenv('EMAIL_USE_TLS'))

EMAIL_USE_SSL: bool = bool(os.getenv('EMAIL_USE_SSL'))

EMAIL_SSL_CERTFILE: str = os.getenv('EMAIL_SSL_CERTFILE')

EMAIL_SSL_KEYFILE: str = os.getenv('EMAIL_SSL_KEYFILE')

EMAIL_TIMEOUT: int = int(os.getenv('EMAIL_TIMEOUT'))


"""Security."""


ACCESS_TOKEN_LIFETIME: int = int(os.getenv('ACCESS_TOKEN_LIFETIME', 0))
ACCESS_TOKEN_LIFETIME_TD: timedelta = timedelta(days=ACCESS_TOKEN_LIFETIME)

SECRET_KEY: str = os.getenv('SECRET_KEY')
