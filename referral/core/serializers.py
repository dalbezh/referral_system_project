from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.utils.translation import gettext_lazy as _

from .models import User


class LoginSerializer(serializers.ModelSerializer):
    """
    Принимает обязательное поле phone_number
    """
    phone_number = serializers.CharField(
        required=True,
        validators=UniqueValidator(queryset=User.objects.all(), message=_("Already exist"))
    )

    def validate(self, attrs):
        pass

    class Meta:
        model = User
        read_only_fields = ("id",)
        fields = ("id", "phone_number", "username", "email")

    def create(self, validated_data):
        instance = User.objects.get_or_create(**validated_data)
        return instance


class LoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = authenticate(
            username=validated_data["username"],
            password=validated_data["password"]
        )
        if not user:
            raise AuthenticationFailedRu
        return user