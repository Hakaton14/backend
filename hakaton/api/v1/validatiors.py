from re import fullmatch

from django.utils.translation import gettext
from rest_framework.serializers import ValidationError

DATE_ERROR: str = gettext(
    "Неверный формат даты. Используйте формат 'YYYY-MM-DD' или 'YYYY-MM'."
)
DATE_PATTERN: str = r'^\w{4}-\d{2}(-\d{2})?$'


def validate_date(value: str) -> str:
    """
    Производит валидацию даты. Допускает указание в форматах:
    'YYYY-MM-DD' или 'YYYY-MM'.
    """
    print(value)
    if not fullmatch(pattern=DATE_PATTERN, string=value):
        raise ValidationError(DATE_ERROR)
    return value
