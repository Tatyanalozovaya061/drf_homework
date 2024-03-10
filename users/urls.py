from django.urls import path
from users import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
    path('create/', views.UserCreate.as_view(), name='user-create'),
    path('detail/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('update/<int:pk>', views.UserUpdate.as_view(), name='user-update'),
    path('delete/<int:pk>', views.UserDelete.as_view(), name='user-delete'),

    path('token/', TokenObtainPairView.as_view(), name='token-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
