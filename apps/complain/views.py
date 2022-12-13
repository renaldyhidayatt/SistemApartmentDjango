from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Complain
from .forms import ComplainForm
from apps.year.models import Year
from apps.month.models import Month
from apps.users.models import Users
from django.contrib import messages


# Create your views here.
class ComplainList(LoginRequiredMixin, ListView):
    model = Complain
    template_name = "complain/index.html"
    context_object_name = "complain_list"


class ComplainCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = ComplainForm()
        year = Year.objects.all()
        month = Month.objects.all()
        user = Users.objects.all()

        context = {"form": form, "year": year, "month": month, "user": user}
        return render(request, "complain/index.html", context)

    def post(self, request):
        form = ComplainForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            date = form.cleaned_data["date"]
            month = request.POST["month"]
            year = request.POST["year"]
            user = request.POST["user"]

            month_id = Month.objects.get(name=month)
            year_id = Year.objects.get(name=year)
            user_id = Users.objects.get(email=user)

            Complain.objects.create(
                title=title,
                description=description,
                date=date,
                month=month_id,
                year=year_id,
                user=user_id,
            )
            messages.success(request, "Berhasil membuat complain")

            return redirect("complain")
        else:
            messages.error(request, "Gagal membuat complain")
            return redirect("complain")


class ComplainUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        complain = Complain.objects.get(id=id)
        form = ComplainForm(instance=complain)

        year = Year.objects.all()
        month = Month.objects.all()
        user = Users.objects.all()

        context = {
            "form": form,
            "year": year,
            "month": month,
            "user": user,
            "complain": complain,
        }
        return render(request, "complain/index.html", context)

    def post(self, request, id):
        form = ComplainForm(request.POST)
        complain = Complain.objects.get(id=id)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            date = form.cleaned_data["date"]
            month = request.POST["month"]
            year = request.POST["year"]
            user = request.POST["user"]

            month_id = Month.objects.get(name=month)
            year_id = Year.objects.get(name=year)
            user_id = Users.objects.get(email=user)

            complain.title = title
            complain.description = description
            complain.date = date
            complain.month = month_id
            complain.year = year_id
            complain.user = user_id

            complain.save()
            messages.success(request, "Berhasil update complain")
            return redirect("complain")
        else:
            messages.error(request, "Gagal update complain")
            return redirect("complain")


@login_required(login_url="/auth/login")
def ComplainDelete(request, id):
    complain = Complain.objects.get(id=id)

    try:
        complain.delete()
        messages.success(request, "Berhasil delete complain")
        return redirect("complain")
    except Complain.DoesNotExist:
        messages.error(request, "Gagal delete complain")
        return redirect("complain")
