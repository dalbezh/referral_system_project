from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("phone_number", "username", "email")
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ("username", "phone_number")
    readonly_fields = ("last_login", "date_joined")
    ordering = ("phone_number",)
    exclude = ("password",)
