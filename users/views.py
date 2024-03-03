from rest_framework import generics, filters
from rest_framework.viewsets import ModelViewSet

from users.models import User, Payment
from users.serializer import UserSerializer, PaymentSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['pay_course', 'pay_lesson', 'pay_method']
    ordering_fields = ['payment_date']
