from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
# TODO: использовать from django.utils.translation import ugettext_lazy
from phonenumber_field.modelfields import PhoneNumberField

from hakaton.app_data import (
    user_avatar_path,
    CITIES_MAX_LEN, DJANGO_HASH_LEN, EMPLOYMENT_MAX_LEN, EXP_MAX_LEN,
    SKILL_CHOICES, SKILLS_CATEGORY_CHOICES, SKILL_MAX_LEN,
    TASK_DESCRIPTION_MAX_LEN, USER_NAME_MAX_LEN,
)
from user.validators import validate_email, validate_name, validate_password


class City(models.Model):
    """Модель городов."""

    name = models.CharField(
        verbose_name='Город',
        max_length=CITIES_MAX_LEN,
        unique=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Employment(models.Model):
    """Модель формата работы."""

    name = models.CharField(
        verbose_name='Формат работы',
        max_length=EMPLOYMENT_MAX_LEN,
        unique=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Формат работы'
        verbose_name_plural = 'Форматы работы'

    def __str__(self):
        return self.name


class Experience(models.Model):
    """Модель срока опыта работы."""

    name = models.CharField(
        verbose_name='Срок опыта работы',
        max_length=EXP_MAX_LEN,
        unique=True,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Срок опыта работы'
        verbose_name_plural = 'Сроки опыта работы'

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    """Модель категорий навыков."""

    name = models.CharField(
        verbose_name='Категория',
        choices=SKILLS_CATEGORY_CHOICES,
        max_length=SKILL_MAX_LEN,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория навыков'
        verbose_name_plural = 'Категории навыков'

    def __str__(self):
        return f'{self.name}'


class Skill(models.Model):
    """Модель навыков."""

    name = models.CharField(
        verbose_name='Навык',
        choices=SKILL_CHOICES,
        max_length=SKILL_MAX_LEN,
        unique=True,
    )
    category = models.ForeignKey(
        verbose_name='Категория',
        to=SkillCategory,
        related_name='skill',
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return f'{self.name}'


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


class UserStudentsFake(models.Model):
    """
    Модель временно имитирует профили студентов на карьерном трекере.
    Здесь и в связанных моделях представлено видение того,
    какие данные должны быть дополнены.
    """

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        validators=(validate_email,),
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=USER_NAME_MAX_LEN,
        validators=(validate_name,),
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=USER_NAME_MAX_LEN,
        validators=(validate_name,),
        blank=True,
        null=True,
    )
    phone = PhoneNumberField(
        verbose_name='Номер телефона',
        region='RU',
        unique=True,
    )
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to=user_avatar_path,
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        verbose_name='Город проживания',
        to=City,
        related_name='user',
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.email


class HrFavorited(models.Model):
    """Модель избранных кандидатов для HR-специалиста."""

    hr = models.ForeignKey(
        verbose_name='HR-специалист',
        to=User,
        related_name='hr_favorite',
        on_delete=models.CASCADE,
    )
    candidate = models.ForeignKey(
        verbose_name='Кандидат',
        to=UserStudentsFake,
        related_name='hr_favorite',
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
        to=User,
        related_name='hr_tasks',
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
        to=User,
        related_name='hr_watched',
        on_delete=models.CASCADE,
    )
    candidate = models.ForeignKey(
        verbose_name='Кандидат',
        to=UserStudentsFake,
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


class UserStudentsFakeEmployment(models.Model):
    """Модель форматов работы студентов."""

    student = models.ForeignKey(
        verbose_name='Студент',
        to=UserStudentsFake,
        related_name='student_employment',
        on_delete=models.CASCADE,
    )
    employment = models.ForeignKey(
        verbose_name='Формат работы',
        to=Employment,
        related_name='student_employment',
        on_delete=models.PROTECT,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('student', 'employment'),
                name='unique_student_employment',
            )
        ]
        ordering = ('-id',)
        verbose_name = 'Формат работы студента'
        verbose_name_plural = 'Форматы работы студентов'

    def __str__(self):
        return (
            f'{self.student.first_name} {self.student.last_name}: '
            f'{self.employment.name}'
        )


class UserStudentsFakeSkill(models.Model):
    """Модель навыков студентов."""

    student = models.ForeignKey(
        verbose_name='Студент',
        to=UserStudentsFake,
        related_name='student_skill',
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        verbose_name='Навык',
        to=Skill,
        related_name='student_skill',
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('student', 'skill'),
                name='unique_student_skill',
            )
        ]
        ordering = ('-id',)
        verbose_name = 'Навыки студента'
        verbose_name_plural = 'Навыки студентов'

    def __str__(self):
        return (
            f'{self.student.first_name} {self.student.last_name}: '
            f'{self.skill.name}'
        )
