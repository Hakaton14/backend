"""
Команда для импорта объектов всех моделей проекта.

Вызов команды осуществляется из папки с manage.py файлом:
python manage.ru csv_db_import.

В команде намеренно не обрабатываются ошибки
и используется except Exception.
В рамках хакатона предполагается, что все scv файлы валидные и согласованные.
"""
import csv
import os

from django.core.management.base import BaseCommand, CommandError
from django.db.models import QuerySet

from vacancy.models import (
    City, Currency, Employment, Experience, Language, LanguageLevel,
    Schedule, Skill, SkillCategory, VacancyStudentStatus,
)
from user.models import User

CSV_BASE_PATH: str = 'user/management/commands/data/'


def import_csv(csv_name: str) -> csv.DictReader:
    """
    Возвращает данные scv файла.
    Значение csv_name для файла some_csv_file.csv
    должно быть указано как 'some_csv_file'.
    """
    full_path: str = f'{CSV_BASE_PATH}{csv_name}.csv'
    if not os.path.exists(full_path):
        raise FileExistsError(f'Файл {csv_name}.csv не предоставлен.')
    return csv.DictReader(
        f=open(file=full_path, encoding='utf-8'),
        delimiter=',',
    )


def import_city() -> None:
    """Импортирует данные в модель City."""
    csv_data: csv.DictReader = import_csv(csv_name='city')
    obj_exists: QuerySet = City.objects.all()
    obj_new: list[City] = []
    for row in csv_data:
        if obj_exists.filter(name=row['name']).exists():
            continue
        obj_new.append(City(**row))
    City.objects.bulk_create(obj_new)


def import_currency() -> None:
    """Импортирует данные в модель Currency."""
    csv_data: csv.DictReader = import_csv(csv_name='currency')
    obj_exists: QuerySet = Currency.objects.all()
    obj_new: list[Currency] = []
    for row in csv_data:
        if obj_exists.filter(name=row['name']).exists():
            continue
        obj_new.append(Currency(**row))
    Currency.objects.bulk_create(obj_new)
    return


def import_employment() -> None:
    """Импортирует данные в модель Employment."""
    csv_data: csv.DictReader = import_csv(csv_name='employment')
    obj_exists: QuerySet = Employment.objects.all()
    obj_new: list[Employment] = []
    for row in csv_data:
        if obj_exists.filter(name=row['name']).exists():
            continue
        obj_new.append(Employment(**row))
    Employment.objects.bulk_create(obj_new)
    return


def import_experience() -> None:
    """Импортирует данные в модель Experience."""
    csv_data: csv.DictReader = import_csv(csv_name='experience')
    obj_exists: QuerySet = Experience.objects.all()
    obj_new: list[Experience] = []
    for row in csv_data:
        if obj_exists.filter(name=row['name']).exists():
            continue
        obj_new.append(Experience(**row))
    Experience.objects.bulk_create(obj_new)
    return


def import_language() -> None:
    """Импортирует данные в модель Language."""
    csv_data: csv.DictReader = import_csv(csv_name='language')
    obj_exists: QuerySet = Language.objects.all()
    obj_new: list[Language] = []
    for row in csv_data:
        if obj_exists.filter(name=row['name']).exists():
            continue
        obj_new.append(Language(**row))
    Language.objects.bulk_create(obj_new)
    return


def import_language_level() -> None:
    """Импортирует данные в модель LanguageLevel."""
    csv_data: csv.DictReader = import_csv(csv_name='language_level')
    obj_exists: QuerySet = LanguageLevel.objects.all()
    obj_new: list[LanguageLevel] = []
    for row in csv_data:
        if obj_exists.filter(name=row['name']).exists():
            continue
        obj_new.append(LanguageLevel(**row))
    LanguageLevel.objects.bulk_create(obj_new)
    return


def import_schedule() -> None:
    """Импортирует данные в модель Currency."""
    csv_data: csv.DictReader = import_csv(csv_name='schedule')
    obj_exists: QuerySet = Schedule.objects.all()
    obj_new: list[Schedule] = []
    for row in csv_data:
        if obj_exists.filter(name=row['name']).exists():
            continue
        obj_new.append(Schedule(**row))
    Schedule.objects.bulk_create(obj_new)
    return


def import_skill_category() -> None:
    """Импортирует данные в модель Skill."""
    csv_data: csv.DictReader = import_csv(csv_name='skill_category')
    obj_exists: QuerySet = SkillCategory.objects.all()
    obj_new: list[SkillCategory] = []
    for row in csv_data:
        if obj_exists.filter(name=row['name']).exists():
            continue
        obj_new.append(SkillCategory(**row))
    SkillCategory.objects.bulk_create(obj_new)
    return


def import_skill() -> None:
    """Импортирует данные в модель SkillCategory."""
    csv_data: csv.DictReader = import_csv(csv_name='skill')
    obj_exists: QuerySet = Skill.objects.all()
    categories_exists: QuerySet = SkillCategory.objects.all()
    obj_new: list[Skill] = []
    for row in csv_data:
        if obj_exists.filter(name=row['name']).exists():
            continue
        if not categories_exists.filter(name=row['category']).exists():
            continue
        obj_new.append(
            Skill(
                name=row['name'],
                category=categories_exists.get(name=row['category'])
            )
        )
    Skill.objects.bulk_create(obj_new)
    return


def import_vacancy_student_status() -> None:
    """Импортирует данные в модель VacancyStudentStatus."""
    csv_data: csv.DictReader = import_csv(csv_name='vacancy_student_status')
    obj_exists: QuerySet = VacancyStudentStatus.objects.all()
    obj_new: list[VacancyStudentStatus] = []
    for row in csv_data:
        if obj_exists.filter(name=row['name']).exists():
            continue
        obj_new.append(VacancyStudentStatus(**row))
    VacancyStudentStatus.objects.bulk_create(obj_new)
    return


def create_admin():
    """Создает модель суперпользователя."""
    email: str = 'admin@email.com'
    password: str = 'admin'
    if not User.objects.filter(email=email):
        User.objects.create_superuser(email=email, password=password)
    return


class Command(BaseCommand):
    help = 'Loading data for all models in project.'

    def handle(self, *args: any, **options: any):
        try:
            import_city()
            import_currency()
            import_employment()
            import_experience()
            import_language()
            import_language_level()
            import_schedule()
            import_skill_category()
            import_skill()
            import_vacancy_student_status()
            create_admin()
        except Exception as err:
            raise CommandError(f'Exception has occurred: {err}')
        return
