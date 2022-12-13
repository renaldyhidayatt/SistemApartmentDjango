from django.shortcuts import render, redirect
from .models import Users
from django.contrib import auth
from django.contrib import messages


# Create your views here.


def loginView(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)

        auth.login(request, user)

        return redirect("dashboard")
    else:
        messages.error(request, "Error Field input")
        return render(request, "auth/login.html")


def registerView(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        email = request.POST["email"]
        password = request.POST["password"]

        user = Users.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        user.save()
        messages.success(request, "Berhasil register")

        return redirect("login")

    else:
        messages.error(request, "Tidak register")
        return render(request, "auth/login.html")


def logoutView(request):
    auth.logout(request)

    return redirect("login")
