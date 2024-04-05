from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from celery import shared_task
from materials.models import Subscription, Course


@shared_task
def send_mail_about_update(course_id):
    course = Course.objects.get(pk=course_id)
    subs = Subscription.objects.all().filter(course=course)
    for sub in subs:
        send_mail(
            subject=f'{course.name}',
            message=f'В {course.name} появились обновления',
            recipient_list=[f'{sub.user.email}'],
            from_email=EMAIL_HOST_USER
        )
