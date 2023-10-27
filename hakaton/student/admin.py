from django.contrib import admin

from hakaton.app_data import ADMIN_LIST_PER_PAGE
from student.models import Student, StudentEmployment, StudentSkill


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
            # TODO: добавить навыки из связной модели
            - город проживания (city)
            - ссылка на фотографию (avatar)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - имя (first_name)
            - фамилия (second_name)
            - электронная почта (email)
            - город проживания (city)
            - номер телефона по стандарту E.164 (phone)
            - ссылка на фотографию (avatar)
        - list_filter (tuple) - список фильтров:
            - имя (first_name)
            - фамилия (second_name)
            # TODO: добавить навыки из связной модели
            - город проживания (city)
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
        'city',
        'avatar',
    )
    list_editable = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'city',
        'avatar',
    )
    list_filter = (
        'first_name',
        'last_name',
        'city',
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
