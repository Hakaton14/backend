from django.db import models

from hakaton.app_data import (
    VACANCY_DESCRIPTION_MAX_LEN, VACANCY_NAME_MAX_LEN,
    VACANCY_STUDENT_STATUS_MAX_LEN, VACANCY_TESTCASE_MAX_LEN,
)
from user.models import City, Grade, Employment, Skill, User, UserStudentsFake


class Vacancy(models.Model):
    """Модель вакансий."""

    hr = models.ForeignKey(
        verbose_name='Ответственный HR',
        to=User,
        related_name='vacancy',
        # TODO: при удалении HR вакансия должна становиться архивной.
        on_delete=models.SET_NULL,
        null=True,
    )
    name = models.CharField(
        verbose_name='Название вакансии',
        max_length=VACANCY_NAME_MAX_LEN,
    )
    city = models.ForeignKey(
        verbose_name='Город',
        to=City,
        related_name='vacancy',
        on_delete=models.PROTECT,
    )
    description = models.TextField(
        verbose_name='Описание вакансии',
        max_length=VACANCY_DESCRIPTION_MAX_LEN,
    )
    salary_from = models.PositiveIntegerField(
        verbose_name='Заработная вилка, от',
    )
    salary_to = models.PositiveIntegerField(
        verbose_name='Заработная вилка, до',
    )
    testcase = models.TextField(
        verbose_name='Тестовый задание для кандидатов',
        max_length=VACANCY_TESTCASE_MAX_LEN,
    )
    grade = models.ForeignKey(
        verbose_name='Требуемый грейд',
        to=Grade,
        related_name='vacancy',
        on_delete=models.PROTECT,
    )
    pub_datetime = models.DateTimeField(
        verbose_name='Дата и время создания вакансии',
        auto_now_add=True,
    )
    # TODO: по истечении этого срока вакансия должна что-то делать?
    deadline_datetime = models.DateTimeField(
        verbose_name='Дата и время дедлайна вакансии',
        default=None,
        blank=True,
        null=True,
    )
    archived = models.BooleanField(
        verbose_name='Статус архивной вакансии',
        default=False,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('hr', 'name', 'description',),
                name='unique_vacancy',
            )
        ]
        ordering = ('-id',)
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.name


class VacancyEmployment(models.Model):
    """Модель перечня форматов работы для вакансии."""

    vacancy = models.ForeignKey(
        verbose_name='Вакансия',
        to=Vacancy,
        related_name='vacancy_employment',
        on_delete=models.CASCADE,
    )
    employment = models.ForeignKey(
        verbose_name='Формат работы',
        to=Employment,
        related_name='vacancy_employment',
        on_delete=models.PROTECT,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('vacancy', 'employment',),
                name='unique_vacancy_employment',
            )
        ]
        ordering = ('-id',)
        verbose_name = 'Формат работы вакансии'
        verbose_name_plural = 'Форматы работы вакансий'

    def __str__(self) -> str:
        return f'{self.vacancy}: {self.employment}'


class VacancyStudentStatus(models.Model):
    """Модель перечня статусов студентов на вакансии."""

    name = models.CharField(
        verbose_name='Статус студента',
        max_length=VACANCY_STUDENT_STATUS_MAX_LEN,
        unique=True,
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Статус студента на вакансии'
        verbose_name_plural = 'Статусы студентов на вакансиях'

    def __str__(self) -> str:
        return self.name


class VacancyFavorited(models.Model):
    """Модель перечня избранных студентов для вакансии и их статус."""

    vacancy = models.ForeignKey(
        verbose_name='Вакансия',
        to=Vacancy,
        related_name='vacancy_favorited',
        on_delete=models.CASCADE,
    )
    student = models.ForeignKey(
        verbose_name='Избранный студент',
        to=UserStudentsFake,
        related_name='vacancy_favorited',
        on_delete=models.CASCADE,
    )
    status = models.ForeignKey(
        verbose_name='Статус кандидата',
        to=VacancyStudentStatus,
        related_name='vacancy_favorited',
        on_delete=models.PROTECT,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('vacancy', 'student',),
                name='unique_vacancy_favorited_student',
            )
        ]
        ordering = ('-id',)
        verbose_name = 'Избранный студент вакансии'
        verbose_name_plural = 'Избранные студенты вакансий'

    def __str__(self) -> str:
        return f'{self.vacancy}: {self.student}'


class VacancySkill(models.Model):
    """Модель перечня требуемых навыков для вакансии."""

    vacancy = models.ForeignKey(
        verbose_name='Вакансия',
        to=Vacancy,
        related_name='vacancy_skill',
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        verbose_name='Навык',
        to=Skill,
        related_name='vacancy_skill',
        on_delete=models.PROTECT,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('vacancy', 'skill',),
                name='unique_vacancy_skill',
            )
        ]
        ordering = ('-id',)
        verbose_name = 'Навык вакансии'
        verbose_name_plural = 'Навыки вакансий'

    def __str__(self) -> str:
        return f'{self.vacancy}: {self.skill}'


class VacancyWatched(models.Model):
    """Модель перечня просмотренных студентов для вакансии."""

    vacancy = models.ForeignKey(
        verbose_name='Вакансия',
        to=Vacancy,
        related_name='vacancy_watched',
        on_delete=models.CASCADE,
    )
    student = models.ForeignKey(
        verbose_name='Просмотренный студент',
        to=UserStudentsFake,
        related_name='vacancy_watched',
        on_delete=models.PROTECT,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('vacancy', 'student',),
                name='unique_vacancy_watched_student',
            )
        ]
        ordering = ('-id',)
        verbose_name = 'Просмотренный студент вакансии'
        verbose_name_plural = 'Просмотренные студенты вакансий'

    def __str__(self) -> str:
        return f'{self.vacancy}: {self.student}'
