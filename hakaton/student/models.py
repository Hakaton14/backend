from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from hakaton.app_data import user_avatar_path, USER_NAME_MAX_LEN
from user.validators import validate_email, validate_name


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

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.email


class StudentEmployment(models.Model):
    """Модель форматов работы студентов."""

    student = models.ForeignKey(
        verbose_name='Студент',
        to='student.Student',
        related_name='student_employment',
        on_delete=models.CASCADE,
    )
    employment = models.ForeignKey(
        verbose_name='Формат работы',
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
        verbose_name = 'Формат работы студента'
        verbose_name_plural = 'Форматы работы студентов'

    def __str__(self):
        return (
            f'{self.student.first_name} {self.student.last_name}: '
            f'{self.employment.name}'
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
