"""
Команда для импорта объектов модели City из csv файла:
user/management/commands/data/cities_rus.csv

Вызов команды осуществляется из папки с manage.py файлом:
python manage.ru csv_cities_import
"""

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from django.db.models import QuerySet

from hakaton.app_data import CITIES_MAX_LEN
from user.models import City
from user.utils import read_csv

CSV_CITIES_PATH: str = 'user/management/commands/data/cities_rus.csv'


def import_cities(cities_list: list[str]) -> None:
    """
    Принимает список названий городов и вносит базу данных те из них,
    которые в ней отсутствуют.

    Args:
        cities_list (list[str]): список названий городов.

    Returns:
        None

    Raises:
        None
    """
    existed_cities_qs: QuerySet = City.objects.all().values_list('name')
    existed_cities: list[str] = [city[0] for city in existed_cities_qs]
    cities: list[City] = []
    for city_name in cities_list:
        if city_name in existed_cities:
            continue
        try:
            if len(city_name) > CITIES_MAX_LEN:
                raise ValidationError(
                    message=(
                        'Введено некорректное название города: '
                        'имя слишком длинное.'
                    )
                )
            cities.append(City(name=city_name))
        except ValidationError as err:
            # TODO: заменить на логгер.
            print(f'Город "{city_name}" не был добавлен: {err}')
    City.objects.bulk_create(cities)
    return


class Command(BaseCommand):
    help = 'Loading cities names from csv.'

    def handle(self, *args: any, **options: any):
        try:
            cities_list: list[dict] = read_csv(full_path=CSV_CITIES_PATH)
            import_cities(cities_list=cities_list)
        except Exception as err:
            raise CommandError(f'Exception has occurred: {err}')
        return
