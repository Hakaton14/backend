from django.contrib import admin

from hakaton.app_data import ADMIN_LIST_PER_PAGE
from student.models import (
    Student, StudentEmployment, StudentLanguage, StudentSchedule, StudentSkill,
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели Student.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - имя (first_name)
            - фамилия (second_name)
            - электронная почта (email)
            - номер телефона по стандарту E.164 (phone)
            - ссылка на страницу vk (link_vk)
            - ссылка на страницу telegram (link_tg)
            - ссылка на страницу facebook (link_fb)
            - ссылка на страницу behance (link_be)
            - ссылка на страницу linkedin (link_in)
            # TODO: добавить навыки из связной модели
            - город проживания (city)
            - готовность к переезду (relocation)
            - специализация (specialization)
            - опыт работы (experience)
            - обо мне (about_me)
            - об опыте (about_exp)
            - об образовании (about_education)
            - ссылка на фотографию (avatar)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - имя (first_name)
            - фамилия (second_name)
            - электронная почта (email)
            - город проживания (city)
            - номер телефона по стандарту E.164 (phone)
            - ссылка на страницу vk (link_vk)
            - ссылка на страницу telegram (link_tg)
            - ссылка на страницу facebook (link_fb)
            - ссылка на страницу behance (link_be)
            - ссылка на страницу linkedin (link_in)
            - готовность к переезду (relocation)
            - специализация (specialization)
            - опыт работы (experience)
            - обо мне (about_me)
            - об опыте (about_exp)
            - об образовании (about_education)
            - ссылка на фотографию (avatar)
        - list_filter (tuple) - список фильтров:
            - имя (first_name)
            - фамилия (second_name)
            # TODO: добавить навыки из связной модели
            - город проживания (city)
            - готовность к переезду (relocation)
            - специализация (specialization)
            - опыт работы (experience)
        - search_fields (tuple) - список полей для поиска объектов:
            - имя (first_name)
            - фамилия (second_name)
            - электронная почта (email)
            - номер телефона по стандарту E.164 (phone)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'phone',
        'link_vk',
        'link_tg',
        'link_fb',
        'link_be',
        'link_in',
        'city',
        'relocation',
        'specialization',
        'experience',
        'about_me',
        'about_exp',
        'about_education',
        'avatar',
    )
    list_editable = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'link_vk',
        'link_tg',
        'link_fb',
        'link_be',
        'link_in',
        'city',
        'relocation',
        'specialization',
        'experience',
        'about_me',
        'about_exp',
        'about_education',
        'avatar',
    )
    list_filter = (
        'first_name',
        'last_name',
        'city',
        'relocation',
        'specialization',
        'experience',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(StudentEmployment)
class StudentEmploymentAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django
    для модели StudentEmployment.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - студент (student)
            - формат работы (employment)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - название (student)
            - формат работы (employment)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'student',
        'employment',
    )
    list_editable = (
        'student',
        'employment',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(StudentSchedule)
class StudentScheduleAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django
    для модели StudentSchedule.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - студент (student)
            - график работы (schedule)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - график работы (schedule)
        - list_filter (tuple) - список фильтров:
            - график работы (schedule)
        - search_fields (tuple) - список полей для поиска объектов:
            - студент (student)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'student',
        'schedule',
    )
    list_editable = (
        'schedule',
    )
    list_filter = (
        'schedule',
    )
    search_fields = (
        'student',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(StudentLanguage)
class StudentLanguageAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django
    для модели StudentLanguage.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - студент (student)
            - разговорный язык (language)
            - уровень владения (level)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - разговорный язык (language)
            - уровень владения (level)
        - list_filter (tuple) - список фильтров:
            - разговорный язык (language)
            - уровень владения (level)
        - search_fields (tuple) - список полей для поиска объектов:
            - студент (student)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'student',
        'language',
        'level',
    )
    list_editable = (
        'language',
        'level',
    )
    list_filter = (
        'language',
        'level',
    )
    search_fields = (
        'student',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(StudentSkill)
class StudentSkillAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели StudentSkill.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - студент (student)
            - навык (skill)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - название (student)
            - навык (skill)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'student',
        'skill',
    )
    list_editable = (
        'student',
        'skill',
    )
    list_per_page = ADMIN_LIST_PER_PAGE
