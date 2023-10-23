from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
# TODO: использовать from django.utils.translation import ugettext_lazy
from phonenumber_field.modelfields import PhoneNumberField


from hakaton.app_data import (
    user_avatar_path,
    CITIES_MAX_LEN, GRADE_CHOICES, GRADE_LEVELS, GRADE_MAX_LEN,
    SKILL_CHOICES, SKILLS_CATEGORY_CHOICES, SKILL_MAX_LEN,
    DJANGO_HASH_LEN, USER_NAME_MAX_LEN,
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


class Grade(models.Model):
    """Модель грейдов."""

    name = models.CharField(
        verbose_name='Грейд',
        choices=GRADE_CHOICES,
        max_length=GRADE_MAX_LEN,
    )
    level = models.IntegerField(
        verbose_name='Уровень грейда',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('level',)
        verbose_name = 'Грейд'
        verbose_name_plural = 'Грейды'

    def save(self, *args, **kwargs):
        self.level: int = GRADE_LEVELS.get(self.name)
        super().save(*args, **kwargs)
        return

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
    grade = models.ForeignKey(
        verbose_name='Грейд',
        to=Grade,
        related_name='student',
        on_delete=models.PROTECT,
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
        verbose_name = 'Избранное для HR'
        verbose_name_plural = 'Избранное для HR'

    def __str__(self):
        return f'{self.hr}: {self.candidate}'


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
        verbose_name = 'Просмотренное для HR'
        verbose_name_plural = 'Просмотренное для HR'

    def __str__(self):
        return f'{self.hr}: {self.candidate}'
