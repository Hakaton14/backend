from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from hakaton.app_data import (
    user_avatar_path,
    STUDENT_ABOUT_MAX_LEN, STUDENT_LINK_MAX_LEN,
    STUDENT_SPEC_MAX_LEN, USER_NAME_MAX_LEN,
)
from user.validators import validate_email, validate_link, validate_name


# TODO: проверить поля сериализатора
class Student(models.Model):
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
    link_vk = models.CharField(
        verbose_name='Ссылка на страницу vk',
        max_length=STUDENT_LINK_MAX_LEN,
        validators=(validate_link,),
        blank=True,
        null=True,
    )
    link_tg = models.CharField(
        verbose_name='Ссылка на страницу telegram',
        max_length=STUDENT_LINK_MAX_LEN,
        validators=(validate_link,),
        blank=True,
        null=True,
    )
    link_fb = models.CharField(
        verbose_name='Ссылка на страницу facebook',
        max_length=STUDENT_LINK_MAX_LEN,
        validators=(validate_link,),
        blank=True,
        null=True,
    )
    link_be = models.CharField(
        verbose_name='Ссылка на страницу behance',
        max_length=STUDENT_LINK_MAX_LEN,
        validators=(validate_link,),
        blank=True,
        null=True,
    )
    link_in = models.CharField(
        verbose_name='Ссылка на страницу linkedin',
        max_length=STUDENT_LINK_MAX_LEN,
        validators=(validate_link,),
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to=user_avatar_path,
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        verbose_name='Город проживания',
        to='vacancy.City',
        related_name='student',
        on_delete=models.PROTECT,
    )
    relocation = models.BooleanField(
        verbose_name='Готовность к переезду',
    )
    specialization = models.CharField(
        verbose_name='Специализация',
        max_length=STUDENT_SPEC_MAX_LEN,
        blank=True,
        null=True,
    )
    experience = models.ForeignKey(
        verbose_name='Опыт работы',
        to='vacancy.Experience',
        related_name='student',
        on_delete=models.PROTECT,
    )
    about_me = models.TextField(
        verbose_name='Обо мне',
        max_length=STUDENT_ABOUT_MAX_LEN,
        blank=True,
        null=True,
    )
    about_exp = models.TextField(
        verbose_name='Об опыте',
        max_length=STUDENT_ABOUT_MAX_LEN,
        blank=True,
        null=True,
    )
    about_education = models.TextField(
        verbose_name='Об образовании',
        max_length=STUDENT_ABOUT_MAX_LEN,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.email


class StudentEmployment(models.Model):
    """Модель возможных типов занятости студентов."""

    student = models.ForeignKey(
        verbose_name='Студент',
        to='student.Student',
        related_name='student_employment',
        on_delete=models.CASCADE,
    )
    employment = models.ForeignKey(
        verbose_name='Тип занятости',
        to='vacancy.Employment',
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
        verbose_name = 'Тип занятости студента'
        verbose_name_plural = 'Типы занятости работы студентов'

    def __str__(self):
        return (
            f'{self.student.first_name} {self.student.last_name}: '
            f'{self.employment.name}'
        )


class StudentLanguage(models.Model):
    """Модель разговорных языков студентов."""

    student = models.ForeignKey(
        verbose_name='Студент',
        to='student.Student',
        related_name='student_language',
        on_delete=models.CASCADE,
    )
    language = models.ForeignKey(
        verbose_name='Разговорный язык',
        to='vacancy.Language',
        related_name='student_language',
        on_delete=models.PROTECT,
    )
    level = models.ForeignKey(
        verbose_name='Уровень владения',
        to='vacancy.LanguageLevel',
        related_name='student_language',
        on_delete=models.PROTECT,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('student', 'language'),
                name='unique_student_language',
            )
        ]
        ordering = ('-id',)
        verbose_name = 'Уровень владения языком'
        verbose_name_plural = 'Уровни владения языками'

    def __str__(self):
        return (
            f'{self.student.first_name} {self.student.last_name}: '
            f'{self.language.name} ({self.level.name})'
        )


class StudentSchedule(models.Model):
    """Модель возможных типов графика работы студентов."""

    student = models.ForeignKey(
        verbose_name='Студент',
        to='student.Student',
        related_name='student_schedule',
        on_delete=models.CASCADE,
    )
    schedule = models.ForeignKey(
        verbose_name='График работы',
        to='vacancy.schedule',
        related_name='student_schedule',
        on_delete=models.PROTECT,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('student', 'schedule'),
                name='unique_student_schedule',
            )
        ]
        ordering = ('-id',)
        verbose_name = 'Тип графика работы студента'
        verbose_name_plural = 'Типы графиков работы студентов'

    def __str__(self):
        return (
            f'{self.student.first_name} {self.student.last_name}: '
            f'{self.schedule.name}'
        )


class StudentSkill(models.Model):
    """Модель навыков студентов."""

    student = models.ForeignKey(
        verbose_name='Студент',
        to='student.Student',
        related_name='student_skill',
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        verbose_name='Навык',
        to='vacancy.Skill',
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
