from datetime import timedelta
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR: Path = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'), verbose=True)


"""Database settings."""


# INFO: пагинация объектов в Django Admin.
ADMIN_LIST_PER_PAGE: int = 15

CITIES_MAX_LEN: int = 30

DB_ENGINE: str = os.getenv('DB_ENGINE')
DB_USER: str = os.getenv('POSTGRES_USER')
DB_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
DB_HOST: str = os.getenv('DB_HOST')
DB_PORT: str = os.getenv('DB_PORT')
DB_NAME: str = os.getenv('POSTGRES_DB')

DB_POSTGRESQL: dict[str, dict[str, str]] = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

DB_SQLITE: dict[str, dict[str, str]] = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DJANGO_HASH_LEN: int = 512

EMPLOYMENT_MAX_LEN: int = 30

GRADE_MAX_LEN: int = 10
GRADE_JUNIOR: str = 'Junior'
GRADE_MIDDLE: str = 'Middle'
GRADE_SENIOR: str = 'Senior'
GRADE_LEAD: str = 'Lead'
GRADE_CHOICES: list[tuple[str]] = [
    (GRADE_JUNIOR, 'Junior'),
    (GRADE_MIDDLE, 'Middle'),
    (GRADE_SENIOR, 'Senior'),
    (GRADE_LEAD, 'Lead'),
]
GRADE_LEVELS: dict[str, int] = {
    GRADE_JUNIOR: 1,
    GRADE_MIDDLE: 2,
    GRADE_SENIOR: 3,
    GRADE_LEAD: 4,
}

SKILL_MAX_LEN: int = 50
SKILLS_CATEGORY_CHOICES = [
    ('Database', 'Базы данных'),
    ('Web-Development', 'Веб-разработка'),
    ('AI/ML', 'Искусственный интеллект и машинное обучение'),
    ('Cloud Technologies', 'Облачные технологии'),
    ('Operating Systems', 'Операционные системы'),
    ('Network Protocols', 'Сетевые протоколы'),
    ('System Administration', 'Системное администрирование'),
    ('Version Control', 'Системы контроля версий'),
    ('Lenguage', 'Язык'),
]
SKILL_CHOICES = [
    # Базы данных.
    ('MySQL', 'MySQL'),
    ('SQL', 'SQL'),
    ('NoSQL (MongoDB, Redis)', 'NoSQL (MongoDB, Redis)'),
    ('Oracle', 'Oracle'),
    ('PostgreSQL', 'PostgreSQL'),

    # Веб-разработка.
    ('Angular', 'Angular'),
    ('Django', 'Django'),
    ('Express.js', 'Express.js'),
    ('HTML/CSS', 'HTML/CSS'),
    ('Node.js', 'Node.js'),
    ('React.js', 'React.js'),
    ('RESTful API', 'RESTful API'),
    ('Vue.js', 'Vue.js'),

    # Искусственный интеллект и машинное обучение.
    ('TensorFlow', 'TensorFlow'),
    ('PyTorch', 'PyTorch'),
    ('Deep Learning', 'Deep Learning'),

    # Облачные технологии.
    ('AWS (Amazon Web Services)', 'AWS (Amazon Web Services)'),
    ('Azure (Microsoft Azure)', 'Azure (Microsoft Azure)'),
    ('DevOps', 'DevOps'),
    ('Google Cloud', 'Google Cloud'),

    # Операционные системы.
    ('Linux', 'Linux'),
    ('Windows Server', 'Windows Server'),

    # Сетевые протоколы.
    ('TCP/IP', 'TCP/IP'),
    ('HTTP/HTTPS', 'HTTP/HTTPS'),

    # Системное администрирование.
    ('Ansible', 'Ansible'),
    ('Linux/Unix администрирование', 'Linux/Unix администрирование'),

    # Системы контроля версий.
    ('Git', 'Git'),
    ('GitHub', 'GitHub'),
    ('GitLab', 'GitLab'),

    # Язык.
    ('C++', 'C++'),
    ('Go', 'Go'),
    ('Java', 'Java'),
    ('JavaScript', 'JavaScript'),
    ('Kotlin', 'Kotlin'),
    ('PHP', 'PHP'),
    ('Python', 'Python'),
    ('Rust', 'Rust'),
    ('Ruby', 'Ruby'),
    ('Swift', 'Swift'),
]

TASK_DESCRIPTION_MAX_LEN: int = 50

VACANCY_DESCRIPTION_MAX_LEN: int = 512
VACANCY_NAME_MAX_LEN: int = 30
VACANCY_STUDENT_STATUS_MAX_LEN: int = 30
VACANCY_TESTCASE_MAX_LEN: int = 512

USER_NAME_MAX_LEN: int = 30

USER_PHOTO_FOLDER: str = 'user/avatar/'


def user_avatar_get_name(user_email: str) -> str:
    """
    Формирует на основании электронной почты пользователя уникальное
    наименование его аватара, заменяя '@' и '.' на '_'.
    Расширение приводится к '.jpg'.
    """
    return (
        f"{user_email.replace('@', '_').replace('.', '_')}.jpg"
    )


def user_avatar_path(instance, filename) -> str:
    """
    Присваивает загружаемому изображению-аватару
    путь с уникальным именем изобажения.
    """
    unique_filename: str = user_avatar_get_name(user_email=instance.email)
    return f'{USER_PHOTO_FOLDER}{unique_filename}'


"""Security."""


ACCESS_TOKEN_LIFETIME: int = int(os.getenv('ACCESS_TOKEN_LIFETIME', 0))
ACCESS_TOKEN_LIFETIME_TD: timedelta = timedelta(days=ACCESS_TOKEN_LIFETIME)

SECRET_KEY: str = os.getenv('SECRET_KEY')
