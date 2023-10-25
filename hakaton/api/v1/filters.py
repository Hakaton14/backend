from rest_framework.filters import BaseFilterBackend

from api.v1.validatiors import validate_date


class TaskMonthFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        date = request.query_params.get('date')
        if not date:
            return queryset
        validate_date(value=date)
        date: list[str] = date.split('-')
        year: int = int(date[0])
        month: int = int(date[1])
        if len(date) > 2:
            day: int = int(date[2])
            queryset = queryset.filter(
                date__year=year,
                date__month=month,
                date__day=day,
            )
        else:
            queryset = queryset.filter(
                date__year=year,
                date__month=month,
            )
        return queryset
