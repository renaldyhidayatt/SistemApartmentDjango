from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .forms import UtilityForm
from .models import Utility
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
class UtilityList(LoginRequiredMixin, ListView):

    model = Utility
    context_object_name = "unit"
    template_name = "utility/index.html"


class UtilityCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = UtilityForm()
        context = {"form": form}
        return render(request, "utility/create.html", context)

    def post(self, request):
        form = UtilityForm(request.POST)
        if form.is_valid():
            gas_bill = form.cleaned_data["gas_bill"]
            security_bill = form.cleaned_data["security_bill"]

            Utility.objects.create(gas_bill=gas_bill, security_bill=security_bill)

            messages.success(request, "Berhasil membuat utility")

            return redirect("utility")
        else:
            messages.error(request, "Gagal membuat utility")

            return redirect("utility")


class UtilityUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        utility = Utility.objects.get(id=id)
        form = UtilityForm(instance=utility)
        context = {"form": form}
        return render(request, "utility/create.html", context)

    def post(self, request, id):
        form = UtilityForm(request.POST)
        if form.is_valid():
            gas_bill = form.cleaned_data["gas_bill"]
            security_bill = form.cleaned_data["security_bill"]

            Utility.objects.create(gas_bill=gas_bill, security_bill=security_bill)

            messages.success(request, "Gagal update utility")

            return redirect("utility")
        else:
            messages.error(request, "Gagal update utility")

            return redirect("utility")


@login_required(login_url="/auth/login")
def UtilityDelete(request, id):
    utility = Utility.objects.get(id=id)
    try:
        utility.delete()
        messages.success(request, "Gagal delete utility")

        return redirect("utility")
    except Utility.DoesNotExist:
        messages.error(request, "Gagal delete utility")

        return redirect("utility")
