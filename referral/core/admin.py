from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "phone_number")
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ('first_name', 'last_name', "username")
    readonly_fields = ("last_login", "date_joined")
    ordering = ('username',)
    exclude = ('password',)
