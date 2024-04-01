from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from users.models import User, Payment
from users.permissions import IsOwner, IsModerator
from users.serializer import UserSerializer, PaymentSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.permissions import IsAuthenticated

from users.services import create_stripe_product_and_price, create_stripe_session


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.save()
        stripe_price_id = create_stripe_product_and_price(payment)
        payment.pay_url, payment.pay_id = create_stripe_session(stripe_price_id)
        payment.save()


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['pay_course', 'pay_lesson', 'pay_method']
    ordering_fields = ['payment_date']


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdate(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]

    def perform_update(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserDelete(generics.DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]
