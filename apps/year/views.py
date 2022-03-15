from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .forms import YearForm
from .models import Year

# Create your views here.
class YearList(ListView):
    model = Year
    template_engine= "year/index.html"
    context_object_name = "year_list"

class YearCreate(View):
    def get(self, request):
        form = YearForm()
        context = {
            "form": form
        }
        return render(request, "year/index.html", context)

    def post(self, request):
        form = YearForm(request.POST)
        if  form.is_valid():
            name = form.cleaned_data["name"]

            Year.objects.create(
                name=name
            )

            return redirect("year")



class YearUpdate(View):
    def get(self, request,id):
        year = Year.objects.get(id=id)
        form = YearForm(instance=year)

        context = {
            "form":form,
            "year": year
        }
        return render(request, "year/update.html", context)

    def post(self, request, id):
        year = Year.objects.get(id=id)
        form = YearForm(request.POST)
        if  form.is_valid():
            name = form.cleaned_data["name"]

            year.name = name
            year.save()

            return redirect("year")


def YearDelete(request,id):
    year = Year.objects.get(id=id)
    try:
        year.delete()
        return redirect("year")
    except Year.DoesNotExist:
        raise Exception("YEar")
