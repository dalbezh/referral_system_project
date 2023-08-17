from django.contrib.auth import login
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from .models import User
from .serializers import LoginSerializer

OTP_CODE = 1234


class LoginView(CreateAPIView):
    """
    Занесение номера телефона в базу
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {
            "status": "OK",
            "user": serializer.data,
            "opt_page": f"http://127.0.0.1:8000/referral/otp/{serializer.data['id']}"
        }

        print(f"Your verify code: {OTP_CODE}")

        return Response(data, status=status.HTTP_201_CREATED)


class VerifyOTPView(UpdateAPIView):
    """
    CBV для авторизации
    """
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if OTP_CODE == int(request.data["otp"]) and instance.phone_number == request.data["phone_number"]:
            instance.is_active = True
            instance.save()

            serializer = self.get_serializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            self.perform_update(instance)
            login(request=request, user=user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"EX": "wrong code"})
