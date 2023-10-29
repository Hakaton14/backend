"""
Команда для импорта объектов всех моделей проекта.

Вызов команды осуществляется из папки с manage.py файлом:
python manage.ru csv_db_import

В команде намеренно не обрабатываются ошибки
и используется except Exception.
В рамках хакатона предполагается, что все scv файлы валидные и согласованные.
"""
import csv
import os

from django.core.management.base import BaseCommand, CommandError
from django.db.models import QuerySet

from student.models import (
    Student, StudentEmployment, StudentLanguage, StudentSchedule, StudentSkill,
)
from vacancy.models import (
    City, Currency, Employment, Experience, Language, LanguageLevel,
    Schedule, Skill, SkillCategory, Vacancy, VacancyLanguage, VacancySkill,
    VacancyStudentStatus,
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


def create_student():
    """Создает объекты разных студентов."""
    csv_data: csv.DictReader = import_csv(csv_name='student')
    obj_exists: QuerySet = Student.objects.all()
    obj_new: list[Student] = []
    student_employment_new: list[StudentEmployment] = []
    student_language_new: list[StudentLanguage] = []
    student_schedule_new: list[StudentSchedule] = []
    student_skill_new: list[StudentSkill] = []
    NUMS: dict[int, str] = {
        1: 'Первый',
        2: 'Второй',
        3: 'Третий',
        4: 'Четвертый',
        5: 'Пятый',
        6: 'Шестой',
        7: 'Седьмой',
        8: 'Восьмой',
    }
    cities: QuerySet = City.objects.all()
    experiences: QuerySet = Experience.objects.all()
    employments: QuerySet = Employment.objects.all()
    languages: QuerySet = Language.objects.all()
    language_levels: QuerySet = LanguageLevel.objects.all()
    schedules: QuerySet = Schedule.objects.all()
    skills: QuerySet = Skill.objects.all()
    for row in csv_data:
        num: int = int(row['num'])
        if obj_exists.filter(id=row['num']).exists():
            continue
        student: Student = Student(
            email=f'email.{num}',
            first_name=f'Иван {NUMS.get(num)}',
            last_name='Иванов',
            phone=f'+7 911 111 11 1{num}',
            link_vk=f'https://vk.com/ivan-{num}/',
            link_tg=f'https://t.me/ivan-{num}/',
            link_fb=f'https://facebbok.com/ivan-{num}/',
            link_be=f'https://behance.com/ivan-{num}/',
            link_in=f'https://linkedin.com/ivan-{num}/',
            city=cities.get(id=row['city']),
            relocation=row['relocation'],
            specialization=f'Специализация №{num}',
            experience=experiences.get(id=row['experience']),
            about_me=f'Тут о студенте №{num}',
            about_exp=f'Тут об опыте студента №{num}',
            about_education=f'Тут об образовании студента №{num}',
        )
        obj_new.append(student)
        student_employment_new.append(
            StudentEmployment(
                student=student,
                employment=employments.get(id=row['employment']),
            )
        )
        row_languages: list[str] = list(row.get('language').split('/'))
        for row_language in row_languages:
            lang_id, level_id = row_language.split('-')
            student_language_new.append(
                StudentLanguage(
                    student=student,
                    language=languages.get(id=lang_id),
                    level=language_levels.get(id=level_id),
                )
            )
        row_schedules: list[str] = list(row.get('schedule').split('/'))
        for schedule_id in row_schedules:
            student_schedule_new.append(
                StudentSchedule(
                    student=student,
                    schedule=schedules.get(id=schedule_id),
                )
            )
        row_skills: list[str] = list(row.get('skill').split('/'))
        for skill_id in row_skills:
            student_skill_new.append(
                StudentSkill(
                    student=student,
                    skill=skills.get(id=skill_id),
                )
            )
    Student.objects.bulk_create(obj_new)
    StudentEmployment.objects.bulk_create(student_employment_new)
    StudentLanguage.objects.bulk_create(student_language_new)
    StudentSchedule.objects.bulk_create(student_schedule_new)
    StudentSkill.objects.bulk_create(student_skill_new)
    return


def create_vacancy():
    """
    Создает вакансию, по требованиям к которой подходят только
    студенты 1 и 2 из объектов в create_student.
    Необходима для тестирования фильтрации по вакансии.
    Вакансия публикуется от имени hr.user@email.com,
    если такого пользователя нет - он будет создан.
    """
    csv_data: csv.DictReader = import_csv(csv_name='vacancy')
    obj_exists: QuerySet = Vacancy.objects.all()
    obj_new: list[Vacancy] = []
    vacancy_language_new: list[VacancyLanguage] = []
    vacancy_skill_new: list[VacancySkill] = []
    if not User.objects.filter(email='hr.user@email.com').exists():
        hr: User = User.objects.create_user(
            email='hr.user@email.com',
            password='MyPass!1',
            first_name='Илона',
            last_name='Маск',
            phone='+7 911 111 22 22',
        )
    else:
        hr: User = User.objects.get(email='hr.user@email.com')
    cities: QuerySet = City.objects.all()
    currencies: QuerySet = Currency.objects.all()
    experiences: QuerySet = Experience.objects.all()
    employments: QuerySet = Employment.objects.all()
    languages: QuerySet = Language.objects.all()
    language_levels: QuerySet = LanguageLevel.objects.all()
    schedules: QuerySet = Schedule.objects.all()
    skills: QuerySet = Skill.objects.all()
    for row in csv_data:
        num: int = int(row['num'])
        name: str = f'Тут название вакансии №{num}'
        if obj_exists.filter(hr=hr, name=name).exists():
            continue
        vacancy: Vacancy = Vacancy(
            hr=hr,
            name=name,
            city=cities.get(id=row['city']),
            address=f'Тут адрес вакансии №{num}',
            description=f'Тут описание вакансии №{num}',
            responsibilities=f'Тут обязанности вакансии №{num}',
            requirements=f'Тут требования вакансии №{num}',
            conditions=f'Тут условия вакансии №{num}',
            salary_from=1000,
            salary_to=2000,
            currency=currencies.get(id=row['currency']),
            testcase=f'Тут тестовое задание вакансии №{num}',
            experience=experiences.get(id=row['experience']),
            employment=employments.get(id=row['employment']),
            schedule=schedules.get(id=row['schedule']),
        )
        obj_new.append(vacancy)
        row_languages: list[str] = list(row['languages'].split('/'))
        for row_language in row_languages:
            lang_id, level_id = row_language.split('-')
            vacancy_language_new.append(
                VacancyLanguage(
                    vacancy=vacancy,
                    language=languages.get(id=lang_id),
                    level=language_levels.get(id=level_id),
                )
            )
        row_skills: list[str] = list(row.get('skills').split('/'))
        for skill_id in row_skills:
            vacancy_skill_new.append(
                VacancySkill(
                    vacancy=vacancy,
                    skill=skills.get(id=skill_id)
                )
            )
    Vacancy.objects.bulk_create(obj_new)
    VacancyLanguage.objects.bulk_create(vacancy_language_new)
    VacancySkill.objects.bulk_create(vacancy_skill_new)
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
            create_student()
            create_vacancy()
        except Exception as err:
            raise CommandError(f'Exception has occurred: {err}')
        return
