from django.contrib.auth import login
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import LoginSerializer, UserCreateSerializer

CODE = "12345"


class LoginView(CreateAPIView):
    """
    Регистрация пользователей
    """
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print(f"2FA code: {CODE}")
            return reverse(viewname="2fa")
        else:
            return Response(
                data={"status": "fail", "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )


class ProfileView(CreateAPIView):
    """
    CBV для авторизации
    """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)
        return Response(serializer.data)
