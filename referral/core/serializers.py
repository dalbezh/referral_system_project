from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.utils.translation import gettext_lazy as _
from phonenumber_field.validators import validate_international_phonenumber

from .models import User


class LoginSerializer(serializers.ModelSerializer):
    """
    Принимает обязательное поле phone_number
    """
    phone_number = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs["phone_number"]:
            validate_international_phonenumber(attrs["phone_number"])
        return attrs

    class Meta:
        model = User
        read_only_fields = ("id", )
        fields = ("id", "phone_number")

    def create(self, validated_data):
        instance, _ = User.objects.get_or_create(**validated_data)
        return instance
