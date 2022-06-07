from django.urls import path
from .views import loginView, registerView

urlpatterns = [
    path("login/", loginView, name="login"),
    path("register/", registerView, name="register"),
]