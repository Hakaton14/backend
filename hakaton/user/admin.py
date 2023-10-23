from django.contrib import admin

from hakaton.app_data import ADMIN_LIST_PER_PAGE
from user.models import (
    City, Grade, HrFavorited, HrWatched, Skill, SkillCategory,
    User, UserStudentsFake
)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели City.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (pk)
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


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели Grade.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (pk)
            - название (name)
            - уровень (level)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'name',
        'level',
    )
    list_per_page = ADMIN_LIST_PER_PAGE


@admin.register(HrFavorited)
class HrFavoritedAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели HrFavorited.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (pk)
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


@admin.register(HrWatched)
class HrWatchedAdmin(admin.ModelAdmin):
    """
    Переопределяет административный интерфейс Django для модели HrWatched.

    Атрибуты:
        - list_display (tuple) - список полей для отображения в интерфейсе:
            - ID (pk)
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
            - ID (pk)
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
            - ID (pk)
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
            - ID (pk)
            - имя (first_name)
            - фамилия (second_name)
            - электронная почта (email)
            - номер телефона по стандарту E.164 (phone)
            - ссылка на фотографию (avatar)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - имя (first_name)
            - фамилия (second_name)
            - электронная почта (email)
            - номер телефона по стандарту E.164 (phone)
            - ссылка на фотографию (avatar)
        - list_filter (tuple) - список фильтров:
            - имя (first_name)
            - фамилия (second_name)
        - search_fields (tuple) - список полей для поиска объектов:
            - имя (first_name)
            - фамилия (second_name)
            - электронная почта (email)
           - номер телефона по стандарту E.164 (phone)
        - list_per_page (int) - количество объектов на одной странице
    """
    list_display = (
        'id',
        'password',
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
            - ID (pk)
            - имя (first_name)
            - фамилия (second_name)
            - электронная почта (email)
            - номер телефона по стандарту E.164 (phone)
            - грейд (grade)
            # TODO: добавить навыки из связной модели
            - город проживания (city)
            - ссылка на фотографию (avatar)
        - list_editable (tuple) - список полей для изменения в интерфейсе:
            - имя (first_name)
            - фамилия (second_name)
            - электронная почта (email)
            - грейд (grade)
            - город проживания (city)
            - номер телефона по стандарту E.164 (phone)
            - ссылка на фотографию (avatar)
        - list_filter (tuple) - список фильтров:
            - имя (first_name)
            - фамилия (second_name)
            - грейд (grade)
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
        'grade',
        'city',
        'avatar',
    )
    list_editable = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'grade',
        'city',
        'avatar',
    )
    list_filter = (
        'first_name',
        'last_name',
        'grade',
        'city',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
    )
    list_per_page = ADMIN_LIST_PER_PAGE
