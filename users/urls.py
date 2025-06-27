from .views import UserRegisterView, UserLoginView
from django.urls import path

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
]
