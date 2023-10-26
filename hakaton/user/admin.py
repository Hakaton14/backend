# TODO: проверить зарегистрированные модели.

from django.contrib import admin

from hakaton.app_data import ADMIN_LIST_PER_PAGE
from user.models import (
    City, Employment, Experience, HrFavorited, HrTask, HrWatched, Skill,
    SkillCategory, User, UserStudentsFake, UserStudentsFakeEmployment,
    UserStudentsFakeSkill,
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


@admin.register(HrFavorited)
class HrFavoritedAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели HrFavorited.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - внешний ключ на User (hr)
            - внешний ключ на UserStudentsFake (candidate)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - внешний ключ на User (hr)
            - внешний ключ на UserStudentsFake (candidate)
        - list_filter (tuple) - список фильтров:
            - внешний ключ на User (hr)
            - внешний ключ на UserStudentsFake (candidate)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'hr',
        'candidate',
    )
    list_editable = (
        'hr',
        'candidate',
    )
    list_filter = (
        'hr',
        'candidate',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(HrTask)
class HrTaskAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели HrTask.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - внешний ключ на User (hr)
            - описание (description)
            - дата (date)
            - время (time)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - описание (description)
            - дата (date)
            - время (time)
        - list_filter (tuple) - список фильтров:
            - внешний ключ на User (hr)
            - дата (date)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'hr',
        'description',
        'date',
        'time',
    )
    list_editable = (
        'description',
        'date',
        'time',
    )
    list_filter = (
        'hr',
        'date',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(HrWatched)
class HrWatchedAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели HrWatched.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - внешний ключ на User (hr)
            - внешний ключ на UserStudentsFake (candidate)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - внешний ключ на User (hr)
            - внешний ключ на UserStudentsFake (candidate)
        - list_filter (tuple) - список фильтров:
            - внешний ключ на User (hr)
            - внешний ключ на UserStudentsFake (candidate)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'hr',
        'candidate',
    )
    list_editable = (
        'hr',
        'candidate',
    )
    list_filter = (
        'hr',
        'candidate',
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


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели User.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (id)
            - имя (first_name)
            - фамилия (last_name)
            - электронная почта (email)
            - номер телефона по стандарту E.164 (phone)
            - ссылка на фотографию (avatar)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - имя (first_name)
            - фамилия (last_name)
            - электронная почта (email)
            - номер телефона по стандарту E.164 (phone)
            - ссылка на фотографию (avatar)
        - list_filter (tuple) - список фильтров:
            - имя (first_name)
            - фамилия (last_name)
        - search_fields (tuple) - список полей для поиска объектов:
            - имя (first_name)
            - фамилия (last_name)
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
        'avatar',
    )
    list_editable = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'avatar',
    )
    list_filter = (
        'first_name',
        'last_name',
    )
    search_fields = (
        'first_name',
        'last_name',
        'phone',
        'email',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(UserStudentsFake)
class UserStudentsFakeAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django
    для модели UserStudentsFake.

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


@admin.register(UserStudentsFakeEmployment)
class UserStudentsFakeEmploymentAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django
    для модели UserStudentsFakeEmployment.

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


@admin.register(UserStudentsFakeSkill)
class UserStudentsFakeSkillAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django
    для модели UserStudentsFakeSkill.

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
