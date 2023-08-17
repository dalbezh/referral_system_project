from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import User


class PasswordlessAuthBackend(ModelBackend):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False

    def get_user(self, user_id):
        try:
           user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
           return None
        return user

    def authenticate(self, request, username=None, phone_number=None, password=None):

        try:
            user = User.objects.get(Q(username=username) | Q(phone_number=phone_number))
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        else:
            return None
