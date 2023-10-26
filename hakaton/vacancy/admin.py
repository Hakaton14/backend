from django.contrib import admin

from hakaton.app_data import ADMIN_LIST_PER_PAGE
from vacancy.models import (
    Vacancy, VacancyEmployment, VacancyFavorited, VacancySkill,
    VacancyStudentStatus, VacancyWatched,
)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели Vacancy.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - ответственный HR (hr)
            - название (name)
            - город (city)
            - описание (description)
            - заработная вилка, от (salary_from)
            - заработная вилка, до (salary_to)
            - тестовое задание (testcase)
            - требуемый грейд (grade)
            - дата и время публикации (pub_datetime)
            - дата и время дедлайна (deadline_datetime)
            - статус архивной (is_archived)
            - статус шаблона (is_template)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - название (name)
            - город (city)
            - описание (description)
            - заработная вилка, от (salary_from)
            - заработная вилка, до (salary_to)
            - тестовое задание (testcase)
            - требуемый грейд (grade)
            - дата и время дедлайна (deadline_datetime)
            - статус архивной (is_archived)
            - статус шаблона (is_template)
        - list_filter (tuple) - список фильтров:
            - ответственный HR (hr)
            - название (name)
            - город (city)
            - заработная вилка, от (salary_from)
            - заработная вилка, до (salary_to)
            - требуемый грейд (grade)
            - статус архивной (is_archived)
            - статус шаблона (is_template)
        - search_fields (tuple) - список полей для поиска объектов:
            - ответственный HR (hr)
            - название (name)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'hr',
        'name',
        'city',
        'description',
        'salary_from',
        'salary_to',
        'testcase',
        'grade',
        'pub_datetime',
        'deadline_datetime',
        'is_archived',
        'is_template',
    )
    list_editable = (
        'name',
        'city',
        'description',
        'salary_from',
        'salary_to',
        'testcase',
        'grade',
        'deadline_datetime',
        'is_archived',
        'is_template',
    )
    list_filter = (
        'hr',
        'name',
        'city',
        'salary_from',
        'salary_to',
        'grade',
        'is_archived',
        'is_template',
    )
    search_fields = (
        'hr',
        'name',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(VacancyEmployment)
class VacancyEmploymentAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django
    для модели VacancyEmployment.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - формат работы (employment)
            - вакансия (vacancy)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - формат работы (employment)
            - вакансия (vacancy)
        - list_filter (tuple) - список фильтров:
            - формат работы (employment)
            - вакансия (vacancy)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'employment',
        'vacancy',
    )
    list_editable = (
        'employment',
        'vacancy',
    )
    list_filter = (
        'employment',
        'vacancy',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(VacancyFavorited)
class VacancyFavoritedAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django
    для модели VacancyFavorited.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - студент (student)
            - вакансия (vacancy)
            - статус студента (status)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - студент (student)
            - вакансия (vacancy)
            - статус студента (status)
        - list_filter (tuple) - список фильтров:
            - студент (student)
            - вакансия (vacancy)
            - статус студента (status)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'student',
        'vacancy',
        'status',
    )
    list_editable = (
        'student',
        'vacancy',
        'status',
    )
    list_filter = (
        'student',
        'vacancy',
        'status',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(VacancySkill)
class VacancySkillAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели VacancySkill.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - вакансия (vacancy)
            - навык (skill)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - вакансия (vacancy)
            - навык (skill)
        - list_filter (tuple) - список фильтров:
            - вакансия (vacancy)
            - навык (skill)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'vacancy',
        'skill',
    )
    list_editable = (
        'vacancy',
        'skill',
    )
    list_filter = (
        'vacancy',
        'skill',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(VacancyStudentStatus)
class VacancyStudentStatusAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django
    для модели VacancyStudentStatus.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - статус студента (name)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - статус студента (name)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'name',
    )
    list_editable = (
        'name',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(VacancyWatched)
class VacancyWatchedAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели VacancyWatched.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - студент (student)
            - вакансия (vacancy)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - студент (student)
            - вакансия (vacancy)
        - list_filter (tuple) - список фильтров:
            - студент (student)
            - вакансия (vacancy)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'student',
        'vacancy',
    )
    list_editable = (
        'student',
        'vacancy',
    )
    list_filter = (
        'student',
        'vacancy',
    )
    list_per_page = ADMIN_LIST_PER_PAGE
