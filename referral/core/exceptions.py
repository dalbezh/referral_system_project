from rest_framework.exceptions import AuthenticationFailed, ValidationError
from django.utils.translation import gettext_lazy as _


class AuthenticationFailedRu(AuthenticationFailed):
    default_detail = _('Некорректный логин или пароль')


class PasswordDontMatch(ValidationError):
    default_detail = _('Пароль не совпадает.')
    default_code = "registration"
