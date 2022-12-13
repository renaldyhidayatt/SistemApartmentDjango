from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Month
from .forms import MonthForm
from django.contrib import messages


# Create your views here.
class MonthList(LoginRequiredMixin, ListView):
    model = Month
    template_name = "month/index.html"
    context_object_name = "month_list"


class MonthCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = MonthForm()
        context = {"form": form}

        return render(request, "month/create.html", context)

    def post(self, request):
        form = MonthForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]

            Month.objects.create(name=name)

            messages.success(request, "Berhasil membuat month")

            return redirect("month")
        else:
            messages.error(request, "Gagal membuat bill")
            return redirect("month")


class MonthUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        month_id = Month.objects.get(id=id)
        form = MonthForm(instance=month_id)
        context = {"form": form, "month": month_id}

        return render(request, "month/update.html", context)

    def post(self, request, id):
        month_id = Month.objects.get(id=id)
        form = MonthForm(request.POST)
        if form.is_valid():
            month_id.name = form.cleaned_data["name"]

            month_id.save()

            messages.success(request, "Berhasil update month")

            return redirect("month")
        else:
            messages.error(request, "Gagal update bill")
            return redirect("month")


@login_required(login_url="/auth/login")
def MonthDelete(request, id):
    month_id = Month.objects.get(id=id)
    try:
        month_id.delete()
        messages.success(request, "berhasil delete month")
        return redirect("month")
    except Month.DoesNotExist:
        messages.error(request, "gagal delete month")
        return redirect("month")
