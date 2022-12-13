from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import YearForm
from .models import Year
from django.contrib import messages

# Create your views here.
class YearList(LoginRequiredMixin, ListView):
    model = Year
    context_object_name = "year_list"
    template_name = "year/index.html"


class YearCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = YearForm()
        context = {"form": form}
        return render(request, "year/index.html", context)

    def post(self, request):
        form = YearForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]

            Year.objects.create(name=name)

            messages.success(request, "Berhasil membuat year")

            return redirect("year")
        else:
            messages.error(request, "Gagal membuat year")

            return redirect("year")


class YearUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        year = Year.objects.get(id=id)
        form = YearForm(instance=year)

        context = {"form": form, "year": year}
        return render(request, "year/update.html", context)

    def post(self, request, id):
        year = Year.objects.get(id=id)
        form = YearForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]

            year.name = name
            year.save()

            messages.success(request, "Berhasil update year")

            return redirect("year")
        else:
            messages.error(request, "Gagal update year")

            return redirect("year")


@login_required(login_url="/auth/login")
def YearDelete(request, id):
    year = Year.objects.get(id=id)
    try:
        year.delete()
        messages.success(request, "Berhasil delete year")

        return redirect("year")
    except Year.DoesNotExist:
        messages.error(request, "Gagal delete year")

        return redirect("year")
