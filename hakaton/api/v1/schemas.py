from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.serializers import CharField, ListField, ModelSerializer

from api.v1.serializers import (
    UserRegisterSerializer, UserUpdateSerializer, VacancySerializer,
)
from vacancy.models import Employment, Schedule, Skill, VacancyLanguage


class VacancyEmploymentSerializer(ModelSerializer):
    """
    Вспомогательный сериализатор для VacancyResponseSchemaSerializer.
    Показывает правильную конфигурацию структуры поля employment
    для retrieve и list запросов.
    """

    class Meta:
        model = Employment
        fields = ('name',)


class VacancyLanguageSerializer(ModelSerializer):
    """
    Вспомогательный сериализатор для VacancyResponseSchemaSerializer.
    Показывает правильную конфигурацию структуры поля languages
    для retrieve и list запросов.
    """

    language = CharField(source='language.name')
    level = CharField(source='level.name')

    class Meta:
        model = VacancyLanguage
        fields = ('language', 'level',)


class VacancyScheduleSerializer(ModelSerializer):
    """
    Вспомогательный сериализатор для VacancyResponseSchemaSerializer.
    Показывает правильную конфигурацию структуры поля schedule
    для retrieve и list запросов.
    """

    class Meta:
        model = Schedule
        fields = ('name',)


class VacancySkillSerializer(ModelSerializer):
    """
    Вспомогательный сериализатор для VacancyResponseSchemaSerializer.
    Показывает правильную конфигурацию структуры поля skill
    для retrieve и list запросов.
    """
    class Meta:
        model = Skill
        fields = ('name',)


class VacancyResponseSchemaSerializer(VacancySerializer):
    """
    Сериализатор используется для корректировки полей
    в drf_spectacular для методов list и retrieve:
        - добавляет список languages
        - добавляет список skills
    """
    employment = VacancyEmploymentSerializer()
    languages = ListField(child=VacancyLanguageSerializer())
    schedule = VacancyScheduleSerializer()
    skills = ListField(child=VacancySkillSerializer())


class LanguageLevelSerializer(ModelSerializer):
    """
    Вспомогательный сериализатор для VacancyRequestSchemaSerializer.
    Показывает правильную конфигурацию структуры поля languages
    для post и update запросов.
    """
    class Meta:
        model = VacancyLanguage
        fields = ('language', 'level',)


class VacancyRequestSchemaSerializer(VacancySerializer):
    """
    Сериализатор используется для корректировки полей
    в drf_spectacular для методов post и update:
        - корректирует список languages
    """
    languages = ListField(child=LanguageLevelSerializer())


CITY_VIEW_SCHEMA: dict[str, str] = {
    'description': (
        'Возвращает список городов.  '
        'При передачи необязательного query параметра search возвращает '
        'список городов, которые начинаются с указанных букв.'
    ),
    'summary': 'Получить список городов.',
    'parameters': [
        OpenApiParameter(
            name='search',
            location=OpenApiParameter.QUERY,
            description='Название навыка.',
            required=False,
            type=str,
        ),
    ],
}

CURRENCY_VIEW_SCHEMA: dict[str, str] = {
    'description': 'Возвращает список валюты.',
    'summary': 'Получить список валюты.',
}

EMPLOYMENT_VIEW_SCHEMA: dict[str, str] = {
    'description': 'Возвращает список форматов работы.',
    'summary': 'Получить список форматов работы.',
}

EXPERIENCE_VIEW_SCHEMA: dict[str, str] = {
    'description': 'Возвращает список сроков опыта работы.',
    'summary': 'Получить список сроков опыта работы.',
}

LANGUAGE_VIEW_SCHEMA: dict[str, str] = {
    'description': 'Возвращает список разговорных языков.',
    'summary': 'Получить список разговорных языков.',
}

LANGUAGE_LEVEL_VIEW_SCHEMA: dict[str, str] = {
    'description': (
        'Возвращает список уровней владения разговорными языками.'
    ),
    'summary': 'Получить список уровней владения разговорными языками.',
}

SCHEDULE_VIEW_SCHEMA: dict[str, str] = {
    'description': 'Возвращает список графиков работы.',
    'summary': 'Получить список графиков работы.',
}

STUDENT_VIEW_SCHEMA: dict[str, str] = {
    'list': extend_schema(
        description=(
            'Возвращает список кандидатов с кратким перечнем полей. '
            'При передачи необязательных query параметра ?from_vacancy '
            'с указанием id вакансии возвращает список кандидатов, '
            'полностью подходящих под ее требованиям. '
            'При передачи необязательных query параметров требований вакансии '
            'возвращает список кандидатов, полностью им удовлетворяющих.'
            'При передачи и ?from_vacancy и параметров вакансии ?from_vacancy '
            'будет в приоритете.'
        ),
        summary='Получить список кандидатов с кратким перечнем полей.',
        parameters=[
            OpenApiParameter(
                name='city',
                location=OpenApiParameter.QUERY,
                description='id города вакансии',
                required=False,
                type=int,
            ),
            OpenApiParameter(
                name='employment',
                location=OpenApiParameter.QUERY,
                description='типа занятости',
                required=False,
                type=int,
            ),
            OpenApiParameter(
                name='from_vacancy',
                location=OpenApiParameter.QUERY,
                description='id вакансии, выдает релевантных ей кандидатов',
                required=False,
                type=int,
            ),
            OpenApiParameter(
                name='experience',
                location=OpenApiParameter.QUERY,
                description='id опыта работы',
                required=False,
                type=int,
            ),
            OpenApiParameter(
                name='language',
                location=OpenApiParameter.QUERY,
                description='перечень id языков и уровня владения ими',
                required=False,
                type=int,
            ),
            OpenApiParameter(
                name='schedule',
                location=OpenApiParameter.QUERY,
                description='id графика работы',
                required=False,
                type=int,
            ),
            OpenApiParameter(
                name='skill',
                location=OpenApiParameter.QUERY,
                description='перечень id навыков',
                required=False,
                type=int,
            ),
        ],
    ),
    'retrieve': extend_schema(
        description=(
            'Возвращает кандидата с указанным идентификатором.'
        ),
        summary='Получить кандидата.',
    ),
}

STUDENT_MARK_WATCHED_SCHEMA: dict[str, str] = {
    'description': 'Отметить кандидата как "просмотрено".',
    'summary': 'Отметить кандидата как "просмотрено".',
    'responses': None,
    'request': None,
}

SKILL_SEARCH_VIEW_SCHEMA: dict[str, str] = {
    'description': (
        'Возвращает список навыков. '
        'При передачи необязательного query параметра search возвращает '
        'список навыков, которые начинаются с указанных букв.'
    ),
    'summary': 'Получить список навыков.',
    'parameters': [
        OpenApiParameter(
            name='search',
            location=OpenApiParameter.QUERY,
            description='Название навыка.',
            required=False,
            type=str,
        ),
    ],
}

SKILL_CATEGORY_VIEW_SCHEMA: dict[str, str] = {
    'description': 'Возвращает список категорий навыков с перечнем навыков.',
    'summary': 'Получить категории навыков с перечнем навыков.',
}

TASK_VIEW_SCHEMA: dict[str, str] = {
    'create': extend_schema(
        description='Создает новую задачу пользователя.',
        summary='Создать задачу пользователя.',
    ),
    'destroy': extend_schema(
        description=(
            'Удаляет задачу пользователя с указанным идентификатором.'
        ),
        summary='Удалить задачу пользователя.',
    ),
    'list': extend_schema(
        description=(
            'Возвращает список задач пользователя. '
            'При передачи необязательного query параметра date в формате '
            'YYYY-MM возвращает список задач за указанный месяц, '
            'в формате YYYY-MM-DD - за указанный день.'
        ),
        summary='Получить список задач пользователя.',
    ),
    'retrieve': extend_schema(
        description=(
            'Возвращает задачу пользователя с указанным идентификатором.'
        ),
        summary='Получить задачу пользователя.',
    ),
    'partial_update': extend_schema(
        description=(
            'Обновляет задачу пользователя.'
        ),
        summary='Обновить задачу пользователя.',
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

VACANCY_VIEW_SCHEMA: dict[str, str] = {
    'create': extend_schema(
        description='Создает новую вакансию пользователя.',
        summary='Создать вакансию пользователя.',
        responses=VacancyResponseSchemaSerializer,
        request=VacancyRequestSchemaSerializer,
    ),
    'list': extend_schema(
        description='Возвращает список вакансий пользователя.',
        summary='Получить список вакансий пользователя.',
        responses=VacancyResponseSchemaSerializer,
    ),
    'retrieve': extend_schema(
        description=(
            'Возвращает вакансию пользователя с указанным идентификатором.'
        ),
        summary='Получить вакансию пользователя.',
        responses=VacancyResponseSchemaSerializer,
        request=VacancyRequestSchemaSerializer,
    ),
    'partial_update': extend_schema(
        description=(
            'Обновляет вакансию пользователя.'
        ),
        summary='Обновить вакансию пользователя.',
        responses=VacancyResponseSchemaSerializer,
    ),
}
