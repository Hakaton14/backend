from re import fullmatch
from django.core.exceptions import ValidationError
from django.utils.translation import gettext

EMAIL_PATTERN: str = r'^(?!\.)[0-9A-Za-z\.]{5,50}@[a-zA-z]+\.[a-zA-z]+$'
EMAIL_ERROR: str = gettext(
    'Можно использовать буквы латинского алфавита (a-z), цифры (0-9) и точки.'
    '\n'
    'Первый символ должен быть латинской буквой или цифрой.'
)

NAME_PATTERN: str = r'^[А-ЯЁа-яё][А-ЯЁа-яё\s\-]{1,30}[А-ЯЁа-яё]$'
NAME_ERROR: str = gettext('Укажите корректное имя или фамилию')

PASS_PATTERN: str = (
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!_@#$%^&+=]).{5,50}$'
)
PASS_ERROR: str = gettext(
    'Введите пароль, который удовлетворяет критериям:\n'
    '    - длина от 5 до 50 символов;\n'
    '    - включает хотя бы одну цифру (0-9);\n'
    '    - включает хотя бы одну прописную букву (a-z);\n'
    '    - включает хотя бы одну заглавную букву (A-Z);\n'
    '    - включает хотя бы один специальный символ (!_@#$%^&+=).'
)


def validate_email(value: str):
    """Производит валидацию поля "email"."""
    if isinstance(value, str) and fullmatch(EMAIL_PATTERN, value):
        return value
    raise ValidationError(EMAIL_ERROR)


def validate_password(value):
    """Производит валидацию поля "password"."""
    if isinstance(value, str) and fullmatch(PASS_PATTERN, value):
        return value
    raise ValidationError(PASS_ERROR)


def validate_name(value):
    """Производит валидацию полей "first_name" и "last_name"."""
    if fullmatch(NAME_PATTERN, value):
        return value
    raise ValidationError(NAME_ERROR)
