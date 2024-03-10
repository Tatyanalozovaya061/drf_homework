from django.contrib import admin

from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ('password',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
