from django.contrib import admin

from hakaton.app_data import ADMIN_LIST_PER_PAGE
from vacancy.models import (
    City, Currency, Employment, Experience, Language, LanguageLevel, Schedule,
    Skill, SkillCategory, Vacancy, VacancyEmployment, VacancyFavorited,
    VacancyLanguage, VacancySkill, VacancyStudentStatus, VacancyWatched,
)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели City.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - название (name)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - название (name)
        - search_fields (tuple) - список полей для поиска объектов:
            - название (name)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'name',
    )
    list_editable = (
        'name',
    )
    search_fields = (
        'name',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели Currency.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - название (name)
            - символ (symbol)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - название (name)
            - символ (symbol)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'name',
        'symbol',
    )
    list_editable = (
        'name',
        'symbol',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели Employment.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - название (name)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - название (name)
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


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели Experience.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - название (name)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - название (name)
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


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели Language.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - название (name)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - название (name)
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


@admin.register(LanguageLevel)
class LanguageLevelAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели LanguageLevel.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - название (name)
            - уровень (level)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - название (name)
            - уровень (level)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'name',
        'level',
    )
    list_editable = (
        'name',
        'level',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели Schedule.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - название (name)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - название (name)
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


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели SkillCategory.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - название (name)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - название (name)
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


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели Skill.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - название (name)
            - категория (category)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - название (name)
            - категория (category)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'name',
        'category',
    )
    list_editable = (
        'name',
        'category',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


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
            - адрес (address)
            - описание (description)
            - обязанности (responsibilities)
            - требования (requirements)
            - условия (conditions)
            - заработная вилка, от (salary_from)
            - заработная вилка, до (salary_to)
            - валюта (currency)
            - тестовое задание (testcase)
            - опыт работы (experience)
            - тип занятости (employment)
            - график работы (schedule)
            - дата и время публикации (pub_datetime)
            - статус архивной (is_archived)
            - статус шаблона (is_template)
            - шаблон письма-приглашения (template_invite)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - название (name)
            - город (city)
            - адрес (address)
            - описание (description)
            - обязанности (responsibilities)
            - требования (requirements)
            - условия (conditions)
            - заработная вилка, от (salary_from)
            - заработная вилка, до (salary_to)
            - валюта (currency)
            - тестовое задание (testcase)
            - опыт работы (experience)
            - тип занятости (employment)
            - график работы (schedule)
            - статус архивной (is_archived)
            - статус шаблона (is_template)
            - шаблон письма-приглашения (template_invite)
        - list_filter (tuple) - список фильтров:
            - ответственный HR (hr)
            - название (name)
            - город (city)
            - заработная вилка, от (salary_from)
            - заработная вилка, до (salary_to)
            - валюта (currency)
            - опыт работы (experience)
            - тип занятости (employment)
            - график работы (schedule)
            - статус архивной (is_archived)
            - статус шаблона (is_template)
        - search_fields (tuple) - список полей для поиска объектов:
            - ответственный HR (hr)
            - название (name)
            - адрес (address)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'hr',
        'name',
        'city',
        'address',
        'description',
        'responsibilities',
        'requirements',
        'conditions',
        'salary_from',
        'salary_to',
        'currency',
        'testcase',
        'experience',
        'employment',
        'schedule',
        'pub_datetime',
        'is_archived',
        'is_template',
        'template_invite',
    )
    list_editable = (
        'name',
        'city',
        'address',
        'description',
        'responsibilities',
        'conditions',
        'salary_from',
        'salary_to',
        'currency',
        'testcase',
        'experience',
        'employment',
        'schedule',
        'is_archived',
        'is_template',
        'template_invite',
    )
    list_filter = (
        'hr',
        'name',
        'city',
        'salary_from',
        'salary_to',
        'currency',
        'experience',
        'employment',
        'schedule',
        'is_archived',
        'is_template',
    )
    search_fields = (
        'hr',
        'name',
        'address'
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


@admin.register(VacancyLanguage)
class VacancyLanguageAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django
    для модели VacancyLanguage.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - вакансия (vacancy)
            - разговорный язык (language)
            - уровень владения (level)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - вакансия (vacancy)
            - разговорный язык (language)
            - уровень владения (level)
        - list_filter (tuple) - список фильтров:
            - вакансия (vacancy)
            - разговорный язык (language)
            - уровень владения (level)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'vacancy',
        'language',
        'level',
    )
    list_editable = (
        'vacancy',
        'language',
        'level',
    )
    list_filter = (
        'vacancy',
        'language',
        'level',
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
