from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import Month
from .forms import MonthForm


# Create your views here.
class MonthList(ListView):
    model = Month
    template_name="month/index.html"
    context_object_name = "month_list"

class MonthCreate(View):
    def get(self, request):
        form = MonthForm()
        context = {
            "form": form
        }

        return render(request, "month/create.html", context)

    def post(self, request):
        form = MonthForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]

            Month.objects.create(
                name=name
            )

            return redirect("month")

class MonthUpdate(View):
    def get(self, request, id):
        month_id = Month.objects.get(id=id)
        form = MonthForm(instance=month_id)
        context = {
            "form": form
        }

        return render(request, "month/update.html", context)

    def post(self, request,id):
        month_id = Month.objects.get(id=id)
        form = MonthForm(request.POST)
        if form.is_valid():
            month_id.name = form.cleaned_data["name"]

            month_id.save()

            return redirect("month")



def MonthDelete(request,id):
    month_id = Month.objects.get(id=id)
    try:
        month_id.delete()
        return redirect("month")
    except Month.DoesNotExist:
        raise Exception("G Bisa")