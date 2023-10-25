import os

from hakaton.app_data import (  # noqa F401
    ACCESS_TOKEN_LIFETIME, BASE_DIR, DB_POSTGRESQL, DB_SQLITE, SECRET_KEY
)


"""App settings."""


# TODO: подключить логгер.
# TODO: Отключить на продакшене. Написать тест, который проверяет это.
DEBUG = True


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
    'djoser',
    'phonenumber_field',
    'api',
    'user',
    'vacancy',
    'drf_spectacular',
]

ROOT_URLCONF = 'hakaton.urls'

SPECTACULAR_SETTINGS = {
    'TITLE': 'Yandex Hakaton API',
    'VERSION': '0.1.0',
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

ALLOWED_HOSTS = []

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
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
   'ACCESS_TOKEN_LIFETIME': ACCESS_TOKEN_LIFETIME,
   'AUTH_HEADER_TYPES': ('Bearer',),
}
