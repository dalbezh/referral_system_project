from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('signup', views.SingUpView.as_view(), name="signup"),
    path('signup/2fa', views.SingUpView.as_view(), name="signup 2fa"),
    path('profile', views.LoginView.as_view(), name="profile"),
    path('verified_code', views.ProfileView.as_view(), name="verified code"),
]