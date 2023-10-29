"""
Список задач для Celery.
"""

from datetime import date

from celery import shared_task
from django.core.mail import send_mail
from django.db.models import QuerySet

from hakaton.settings import DEFAULT_FROM_EMAIL
from user.models import User


@shared_task
def send_hr_task_notify() -> None:
    """Посылает HR-специалистам рассылку с их задачами на сегодня."""
    today: date = date.today()
    users_with_todo: QuerySet = User.objects.prefetch_related(
        'hr_task'
    ).filter(
        hr_task__date=today
    )
    for user in users_with_todo:
        tasks_for_user = [
            (f'{task.time}: {task.description}')
            for task in user.hr_task.filter(date=today)
        ]
        send_mail(
            subject='Ваши задачи на сегодня',
            message='\n'.join(tasks_for_user),
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=(user.email,),
            fail_silently=False,
        )
    return
