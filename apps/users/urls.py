from django.urls import path
from .views import loginView, registerView, logoutView

urlpatterns = [
    path("login/", loginView, name="login"),
    path("logout/", logoutView, name="logout"),
    path("register/", registerView, name="register"),
]
