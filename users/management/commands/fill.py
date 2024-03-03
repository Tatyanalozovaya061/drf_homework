from django.core.management import BaseCommand

from users.models import Payment


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Payment.objects.all().delete()

        paymant_list = [{
            'user': 'user1',
            'pay_date': '2023-09-01',
            'pay_course': 'course1',
            'pay_amount': '99999.00',
        },
            {
            'user': 'user2',
            'pay_date': '2023-08-01',
            'pay_lesson': 'lesson1',
            'pay_amount': '999.00',
        },
        ]

        payments = []
        for payment_item in paymant_list:
            payments.append(Payment(**payment_item))

        Payment.objects.bulk_create(payments)
