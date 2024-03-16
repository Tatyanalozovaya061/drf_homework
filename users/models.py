from django.db import models
from django.contrib.auth.models import AbstractUser

from materials.models import Course, Lesson

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=20, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    pay_date = models.DateField(verbose_name='дата оплаты', **NULLABLE)
    pay_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    pay_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    pay_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма оплаты')
    pay_method = models.CharField(max_length=20, choices=[('cash', 'наличные'), ('transfer', 'перевод на счет')],
                                  verbose_name='тип оплаты')

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

    def __str__(self):
        return f'Платеж {self.user}'
