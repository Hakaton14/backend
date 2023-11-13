import os

from corsheaders.defaults import default_headers
from celery.schedules import crontab

from hakaton.app_data import (  # noqa F401
    ACCESS_TOKEN_LIFETIME_TD, BASE_DIR, CITE_DOMAIN, CITE_IP, DB_POSTGRESQL,
    DB_SQLITE, DEFAULT_FROM_EMAIL, EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER,
    EMAIL_HOST_PASSWORD, EMAIL_USE_TLS, EMAIL_USE_SSL, EMAIL_SSL_CERTFILE,
    EMAIL_SSL_KEYFILE, EMAIL_TIMEOUT, SECRET_KEY,
)


"""App settings."""


# TODO: подключить логгер.
DEBUG = False


"""Celery settings."""


CELERY_TIMEZONE = 'Europe/Moscow'

CELERY_BEAT_SCHEDULE = {
    'send_hr_task_notify': {
        'task': 'user.tasks.send_hr_task_notify',
        'schedule': crontab(hour=7),
    },
}

CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

CELERY_BROKER_URL = 'redis://hr_practicum_redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://hr_practicum_redis:6379/0'


"""Email settings."""


if DEBUG:
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_HOST: str = EMAIL_HOST
EMAIL_PORT: int = EMAIL_PORT
EMAIL_HOST_USER: str = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD: str = EMAIL_HOST_PASSWORD
EMAIL_USE_TLS: bool = EMAIL_USE_TLS
EMAIL_USE_SSL: bool = EMAIL_USE_SSL
EMAIL_SSL_CERTFILE: str = EMAIL_SSL_CERTFILE
EMAIL_SSL_KEYFILE: str = EMAIL_SSL_KEYFILE
EMAIL_TIMEOUT: int = EMAIL_TIMEOUT


"""Django settings."""


AUTH_USER_MODEL = 'user.User'

DATABASES = DB_POSTGRESQL

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_celery_beat',
    'django_filters',
    'djoser',
    'corsheaders',
    'phonenumber_field',
    'api',
    'student',
    'user',
    'vacancy',
    'drf_spectacular',
]

ROOT_URLCONF = 'hakaton.urls'

SPECTACULAR_SETTINGS = {
    'TITLE': 'Yandex Hakaton API',
    'VERSION': '0.6.0',
    'DESCRIPTION': 'Team 14',
    'CONTACT': {
        'name': 'Kirill Svidunovich',
        'url': 'https://github.com/TheSuncatcher222',
        'email': 'TheSuncatcher222@gmail.com',
    },
    'SERVE_INCLUDE_SCHEMA': False,
    'SCHEMA_PATH_PREFIX': r'/api/v1/',
    'SCHEMA_COERCE_PATH_PK_SUFFIX': True,
    'SORT_OPERATIONS': True,
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hakaton.wsgi.application'


"""Static files settings."""


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = 'media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = 'static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


"""Regional settings."""


LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


"""Security settings."""


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ALLOWED_HOSTS = [CITE_DOMAIN, CITE_IP, '127.0.0.1', 'localhost']

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    *default_headers,
    'access-control-allow-credentials',
    'Access-Control-Allow-Headers',
    'Access-Control-Allow-Credentials',
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    f'http://{CITE_DOMAIN}',
    f'http://{CITE_IP}:8000',
    f'https://{CITE_DOMAIN}',
    f'https://{CITE_IP}:8000',
]

CSRF_TRUSTED_ORIGINS = [
    f'https://{CITE_DOMAIN}',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SECRET_KEY = SECRET_KEY

SIMPLE_JWT = {
   'ACCESS_TOKEN_LIFETIME': ACCESS_TOKEN_LIFETIME_TD,
   'AUTH_HEADER_TYPES': ('Bearer',),
}
