from django.conf import settings
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='название курса')
    image = models.ImageField(upload_to='courses/', verbose_name='картинка курса', **NULLABLE)
    description = models.TextField(verbose_name='описание курса')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def str(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='название урока', unique=True)
    image = models.ImageField(upload_to='lessons/', verbose_name='картинка урока', **NULLABLE)
    description = models.TextField(verbose_name='описание урока')
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def str(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='подписчик')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
