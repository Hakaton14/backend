# TODO: возможно стоит вынести навыки, языки и т.п. в отдельный модуль.
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
# TODO: использовать from django.utils.translation import ugettext_lazy
from phonenumber_field.modelfields import PhoneNumberField

from hakaton.app_data import (
    user_avatar_path,
    DJANGO_HASH_LEN, TASK_DESCRIPTION_MAX_LEN, USER_NAME_MAX_LEN,
)
from user.validators import validate_email, validate_name, validate_password


class UserManager(BaseUserManager):
    """Менеджер по созданию и управлению пользователями."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Создает и сохраняет пользователя с полученными почтой и паролем."""
        email = self.normalize_email(email).lower()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        """Переопределяет метод создания пользователя."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Переопределяет метод создания пользователя-администратора."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Модель HR-специалиста."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        validators=(validate_email,),
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=USER_NAME_MAX_LEN,
        validators=(validate_name,),
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=USER_NAME_MAX_LEN,
        validators=(validate_name,),
    )
    password = models.CharField(
        verbose_name='Пароль',
        # INFO: не изменять, Django создает длинный хэш паролей!
        max_length=DJANGO_HASH_LEN,
        validators=(validate_password,)
    )
    phone = PhoneNumberField(
        verbose_name='Номер телефона',
        region='RU',
        unique=True,
    )
    # TODO: подключить сигнал на удаление картинки при удалении объекта.
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to=user_avatar_path,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name='Статус активного',
        default=True,
    )
    is_staff = models.BooleanField(
        verbose_name='Статус администратора',
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name='Статус суперпользователя',
        default=False,
    )
    date_joined = models.DateTimeField(
        verbose_name='Дата регистрации',
        auto_now_add=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ('-id',)
        verbose_name = 'HR специалист'
        verbose_name_plural = 'HR специалисты'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class HrFavorited(models.Model):
    """Модель избранных кандидатов для HR-специалиста."""

    hr = models.ForeignKey(
        verbose_name='HR-специалист',
        to='user.User',
        related_name='hr_favorited',
        on_delete=models.CASCADE,
    )
    candidate = models.ForeignKey(
        verbose_name='Кандидат',
        to='student.Student',
        related_name='hr_favorited',
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('hr', 'candidate'),
                name='unique_candidate_hr_favorite',
            )
        ]
        ordering = ('-id',)
        verbose_name = 'Избранное для HR специалиста'
        verbose_name_plural = 'Избранное для HR специалистов'

    def __str__(self):
        return f'{self.hr}: {self.candidate}'


class HrTask(models.Model):
    """Модель задач календаря HR-специалиста."""

    hr = models.ForeignKey(
        verbose_name='HR-специалист',
        to='user.User',
        related_name='hr_task',
        on_delete=models.CASCADE,
    )
    description = models.CharField(
        verbose_name='Описание задачи',
        max_length=TASK_DESCRIPTION_MAX_LEN,
    )
    date = models.DateField(
        verbose_name='Дата задачи',
    )
    time = models.TimeField(
        verbose_name='Время задачи',
    )

    class Meta:
        ordering = ('date', 'time',)
        verbose_name = 'Задача HR-специалиста'
        verbose_name_plural = 'Задачи HR-специалистов'

    def __str__(self):
        return f'{self.date} {self.time}: {self.description}'


class HrWatched(models.Model):
    """
    Модель реестра просмотренных кандидатов для HR-специалиста
    при глобальном поиске.
    """

    hr = models.ForeignKey(
        verbose_name='HR-специалист',
        to='user.User',
        related_name='hr_watched',
        on_delete=models.CASCADE,
    )
    candidate = models.ForeignKey(
        verbose_name='Кандидат',
        to='student.Student',
        related_name='hr_watched',
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('hr', 'candidate'),
                name='unique_candidate_hr_watched',
            )
        ]
        ordering = ('-id',)
        verbose_name = 'Просмотренное для HR специалиста'
        verbose_name_plural = 'Просмотренное для HR специалистов'

    def __str__(self):
        return f'{self.hr}: {self.candidate}'
