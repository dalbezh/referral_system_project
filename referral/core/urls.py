from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('login', views.LoginView.as_view(), name="login"),
    path('otp/<pk>', views.VerifyOTPView.as_view(), name="otp"),
]
