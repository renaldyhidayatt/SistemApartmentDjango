from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from apps.year.models import Year
from apps.month.models import Month
from .models import Maintance
from .forms import MaintanceForm

# Create your views here.

class MaintanceList(ListView):
    model = Maintance
    template_name = "maintance/index.html"
    context_object_name = "maintance_list"
    


class MaintanceCreate(View):
    def get(self, request):
        form = MaintanceForm()
        month = Month.objects.all()
        year = Year.objects.all()

        context = {
            "form": form,
            "month": month,
            "year": year
        }

        return render(request, "maintance/create.html", context)

    def post(self, request):
        form = MaintanceForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            date = form.cleaned_data["date"]
            amount = form.cleaned_data["amount"]
            details = form.cleaned_data["details"]
            month = request.POST["month"]
            year = request.POST["year"]

            month_id = Month.objects.get(name=month)
            year_id = Year.objects.get(name=year)

            Maintance.objects.create(
                title=title,
                date=date,
                amount=amount,
                details=details,
                month=month_id,
                year=year_id
            )

            return redirect("maintance")
            

class MaintanceUpdate(View):
    def get(self, request, id):
        maintance= Maintance.objects.get(id=id)
        form = MaintanceForm(instance=maintance)
        month = Month.objects.all()
        year = Year.objects.all()

        context = {
            "form": form,
            "month": month,
            "year": year,
            "maintance": maintance
        }

        return render(request, "maintance/create.html", context)

    def post(self,request,id):
        maintance = Maintance.objects.get(id=id)
        form = MaintanceForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            date = form.cleaned_data["date"]
            amount = form.cleaned_data["amount"]
            details = form.cleaned_data["details"]
            month = request.POST["month"]
            year = request.POST["year"]

            month_id = Month.objects.get(name=month)
            year_id = Year.objects.get(name=year)

            maintance.title = title
            maintance.date =date
            maintance.amount = amount
            maintance.details = details
            maintance.month = month_id
            maintance.year = year_id

            maintance.save()

            return redirect("maintance")


def MaintanceDelete(request,id):
    maintance = Maintance.objects.get(id=id)

    try:
        maintance.delete()
        return redirect("maintance")
    except Maintance.DoesNotExist:
        raise Exception("Maintance")