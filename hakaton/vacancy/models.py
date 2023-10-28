from django.db import models

from hakaton.app_data import (
    CITIES_MAX_LEN, CURRENCY_MAX_LEN, CURRENCY_SYMBOL_MAX_LEN,
    EMPLOYMENT_MAX_LEN, EXP_MAX_LEN, LANGUAGE_MAX_LEN, LANGUAGE_LEVEL_MAX_LEN,
    SCHEDULE_MAX_LEN, SKILL_MAX_LEN, VACANCY_NAME_MAX_LEN,
    VACANCY_ADDRESS_MAX_LEN, VACANCY_STUDENT_STATUS_MAX_LEN,
    VACANCY_TEMPLATE_INVITE, VACANCY_TEXT_MAX_LEN,
)


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


class Currency(models.Model):
    """Модель валют."""

    name = models.CharField(
        verbose_name='Название валюты',
        max_length=CURRENCY_MAX_LEN,
        unique=True,
    )
    symbol = models.CharField(
        verbose_name='Символ',
        max_length=CURRENCY_SYMBOL_MAX_LEN,
        unique=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'symbol',),
                name='unique_name_symbols',
            )
        ]
        ordering = ('name',)
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return f'{self.name} ({self.symbol})'


class Employment(models.Model):
    """Модель типа занятости."""

    name = models.CharField(
        verbose_name='Тип занятости',
        max_length=EMPLOYMENT_MAX_LEN,
        unique=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип занятости'
        verbose_name_plural = 'Типы занятости'

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


class Language(models.Model):
    """Модель разговорных языков."""

    name = models.CharField(
        verbose_name='Название языка',
        max_length=LANGUAGE_MAX_LEN,
        unique=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Название языка'
        verbose_name_plural = 'Названия языков'

    def __str__(self):
        return self.name


class LanguageLevel(models.Model):
    """Уровень владения разговорным языком языком"""

    name = models.CharField(
        verbose_name='Название',
        max_length=LANGUAGE_LEVEL_MAX_LEN,
        unique=True,
    )
    level = models.IntegerField(
        verbose_name='Уровень владения',
        unique=True,
    )

    class Meta:
        ordering = ('level',)
        verbose_name = 'Уровень владения языком'
        verbose_name_plural = 'Уровни владения языками'

    def __str__(self):
        return self.name


class Schedule(models.Model):
    """Модель графика работы."""

    name = models.CharField(
        verbose_name='График работы',
        max_length=SCHEDULE_MAX_LEN,
        unique=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    """Модель категорий навыков."""

    name = models.CharField(
        verbose_name='Категория',
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
        max_length=SKILL_MAX_LEN,
        unique=True,
    )
    category = models.ForeignKey(
        verbose_name='Категория',
        to='vacancy.SkillCategory',
        related_name='skill',
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return f'{self.name}'


class Vacancy(models.Model):
    """Модель вакансий."""

    hr = models.ForeignKey(
        verbose_name='Ответственный HR',
        to='user.User',
        related_name='vacancy',
        # TODO: при удалении HR вакансия должна становиться архивной.
        on_delete=models.SET_NULL,
        null=True,
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=VACANCY_NAME_MAX_LEN,
    )
    city = models.ForeignKey(
        verbose_name='Город',
        to='vacancy.City',
        related_name='vacancy',
        on_delete=models.PROTECT,
    )
    address = models.CharField(
        verbose_name='Адрес офиса',
        max_length=VACANCY_ADDRESS_MAX_LEN,
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=VACANCY_TEXT_MAX_LEN,
        default=None,
        blank=True,
        null=True,
    )
    responsibilities = models.TextField(
        verbose_name='Обязанности',
        max_length=VACANCY_TEXT_MAX_LEN,
    )
    requirements = models.TextField(
        verbose_name='Описание',
        max_length=VACANCY_TEXT_MAX_LEN,
    )
    conditions = models.TextField(
        verbose_name='Условия',
        max_length=VACANCY_TEXT_MAX_LEN,
    )
    salary_from = models.PositiveIntegerField(
        verbose_name='Заработная вилка, от',
    )
    salary_to = models.PositiveIntegerField(
        verbose_name='Заработная вилка, до',
    )
    currency = models.ForeignKey(
        verbose_name='Валюта',
        to='vacancy.Currency',
        related_name='vacancy',
        on_delete=models.PROTECT,
    )
    testcase = models.TextField(
        verbose_name='Тестовый задание для кандидатов',
        max_length=VACANCY_TEXT_MAX_LEN,
        default=None,
        blank=True,
        null=True
    )
    experience = models.ForeignKey(
        verbose_name='Опыт работы',
        to='vacancy.Experience',
        related_name='vacancy',
        on_delete=models.PROTECT,
    )
    employment = models.ForeignKey(
        verbose_name='Тип занятости',
        to='vacancy.Employment',
        related_name='vacancy',
        on_delete=models.PROTECT,
    )
    schedule = models.ForeignKey(
        verbose_name='График работы',
        to='vacancy.Schedule',
        related_name='vacancy',
        on_delete=models.PROTECT,
    )
    pub_datetime = models.DateTimeField(
        verbose_name='Дата и время создания',
        auto_now_add=True,
    )
    is_archived = models.BooleanField(
        verbose_name='Статус архивной',
        default=False,
    )
    is_template = models.BooleanField(
        verbose_name='Статус шаблона',
        default=False,
    )
    template_invite = models.TextField(
        verbose_name='Шаблон письма-приглашения',
        max_length=VACANCY_TEXT_MAX_LEN,
        default=VACANCY_TEMPLATE_INVITE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'description',),
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
        to='vacancy.Vacancy',
        related_name='vacancy_employment',
        on_delete=models.CASCADE,
    )
    employment = models.ForeignKey(
        verbose_name='Формат работы',
        to='vacancy.Employment',
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


class VacancyLanguage(models.Model):
    """
    Модель перечня требуемых уровней владения
    разговорными языками для вакансии.
    """

    vacancy = models.ForeignKey(
        verbose_name='Вакансия',
        to='vacancy.Vacancy',
        related_name='vacancy_language',
        on_delete=models.CASCADE,
    )
    language = models.ForeignKey(
        verbose_name='Разговорный язык',
        to='vacancy.Language',
        related_name='vacancy_language',
        on_delete=models.PROTECT,
    )
    level = models.ForeignKey(
        verbose_name='Уровень владения',
        to='vacancy.LanguageLevel',
        related_name='vacancy_language',
        on_delete=models.PROTECT,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('vacancy', 'language', 'level',),
                name='unique_vacancy_language_level',
            )
        ]
        ordering = ('vacancy', 'language',)
        verbose_name = 'Требуемый уровень владения языка'
        verbose_name_plural = 'Требования к владению языкам'

    def __str__(self) -> str:
        return f'{self.language} ({self.level})'


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
        to='vacancy.Vacancy',
        related_name='vacancy_favorited',
        on_delete=models.CASCADE,
    )
    student = models.ForeignKey(
        verbose_name='Избранный студент',
        to='student.Student',
        related_name='vacancy_favorited',
        on_delete=models.CASCADE,
    )
    status = models.ForeignKey(
        verbose_name='Статус кандидата',
        to='vacancy.VacancyStudentStatus',
        related_name='vacancy_favorited',
        on_delete=models.PROTECT,
        default=None,
        blank=True,
        null=True,
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
        to='vacancy.Vacancy',
        related_name='vacancy_skill',
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        verbose_name='Навык',
        to='vacancy.Skill',
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
        to='vacancy.Vacancy',
        related_name='vacancy_watched',
        on_delete=models.CASCADE,
    )
    student = models.ForeignKey(
        verbose_name='Просмотренный студент',
        to='student.Student',
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
