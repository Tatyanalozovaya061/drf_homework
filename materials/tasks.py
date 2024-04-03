from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from celery import shared_task
from materials.models import Subscription


@shared_task
def send_mail_about_update(course):
    subs = Subscription.objects.all().filter(course=course)
    users = []
    for sub in subs:
        users.append(sub.user)
    for user in users:
        message = f'{course.name} обновлен'
        send_mail(
            subject='обновление курса',
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
