from django.contrib import admin

from hakaton.app_data import ADMIN_LIST_PER_PAGE
from user.models import HrFavorited, HrTask, HrWatched, User


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
