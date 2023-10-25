from django.db.models import QuerySet
from rest_framework.filters import BaseFilterBackend

from api.v1.validatiors import validate_date


class TaskMonthFilter(BaseFilterBackend):
    """
    Фильтр query параметра "date" для TaskViewSet.
    Производит валидацию на соответствие даты паттерну:
        - YYYY-MM-DD: возвращает queryset, все задачи,
                      у которых date соответствует дате
        - YYYY-MM: возвращает list[int],
                   список дней, когда есть хотя бы одна задача
    Возвращает ValidationError, если query параметр не соответствует.
    """
    def filter_queryset(self, request, queryset, view):
        date: str = request.query_params.get('date')
        if not date:
            return queryset
        validate_date(value=date)
        date: list[str] = date.split('-')
        year: int = int(date[0])
        month: int = int(date[1])
        if len(date) > 2:
            day: int = int(date[2])
            queryset: QuerySet = queryset.filter(
                date__year=year,
                date__month=month,
                date__day=day,
            )
            return queryset
        queryset: QuerySet = queryset.filter(
            date__year=year,
            date__month=month,
        )
        days_with_tasks: list[int] = queryset.values_list(
            'date__day', flat=True
        ).distinct()
        return days_with_tasks
