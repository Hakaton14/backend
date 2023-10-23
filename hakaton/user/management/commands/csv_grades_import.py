"""
Команда для импорта объектов модели Grade из csv файла:
user/management/commands/data/cities_rus.csv

Вызов команды осуществляется из папки с manage.py файлом:
python manage.ru csv_cities_import
"""

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from django.db.models import QuerySet

from hakaton.app_data import GRADE_LEVELS
from user.utils import read_csv
from user.models import Grade

CSV_GRADES_PATH: str = 'user/management/commands/data/grades.csv'


def import_grades(grades_list: list[str]) -> None:
    """
    Принимает список названий грейдов и вносит базу данных те из них,
    которые в ней отсутствуют.

    Args:
        cities_list (list[str]): список названий грейдов.

    Returns:
        None

    Raises:
        None
    """
    existed_grades_qs: QuerySet = Grade.objects.all().values_list('name')
    existed_grades: list[str] = [grade[0] for grade in existed_grades_qs]
    grades: list[Grade] = []
    for grade_name in grades_list:
        if grade_name in existed_grades:
            continue
        if grade_name not in GRADE_LEVELS:
            raise ValidationError(
                message='Указан недействительный грейд.'
            )
        try:
            grades.append(
                Grade(
                    name=grade_name,
                    level=GRADE_LEVELS.get(grade_name)
                )
            )
        except ValidationError as err:
            # TODO: заменить на логгер.
            print(f'Грейд "{grade_name}" не был добавлен: {err}')
    Grade.objects.bulk_create(grades)
    return


class Command(BaseCommand):
    help = 'Loading grades names from csv.'

    def handle(self, *args: any, **options: any):
        try:
            grades_list: list[dict] = read_csv(full_path=CSV_GRADES_PATH)
            import_grades(grades_list=grades_list)
        except Exception as err:
            raise CommandError(f'Exception has occurred: {err}')
        return
