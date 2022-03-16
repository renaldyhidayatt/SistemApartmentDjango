from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Rent
from .forms import RentForm
from apps.floor.models import Floor
from apps.unit.models import Unit
from apps.month.models import Month
from apps.year.models import Year
from apps.branch.models import Branch



# Create your views here.
class RentList(ListView):
    model = Rent
    template_name = "rent/index.html"
    context_object_name = "rent_list"


class RentCreate(View):
    def get(self, request):
        form = RentForm()
        floor = Floor.objects.all()
        unit = Unit.objects.all()
        month = Month.objects.all()
        year = Year.objects.all()
        branch = Branch.objects.all()

        context = {
            "form": form,
            "floor": floor,
            "unit": unit,
            "month": month,
            "year": year,
            "branch": branch
        }

        return render(request, "rent/create.html",context)

    def post(self, request):
        form = RentForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data["address"]
            nid = form.cleaned_data["nid"]
            floor = request.POST["floor"]
            unit = request.POST["unit"]
            advance = form.cleaned_data["advance"]
            rent_pm = form.changed_data["rent_pm"]
            date = form.cleaned_data["date"]
            month = request.POST["month"]
            year = request.POST["year"]
            branch = request.POST["branch"]

            month_id = Month.objects.get(name=month)
            year_id = Year.objects.get(name=year)
            floor_id = Floor.objects.get(floor_no=floor)
            unit_id = Unit.objects.get(unit_no=unit)
            branch_id = Branch.objects.get(name=branch)

            Rent.objects.create(
                month=month_id,
                year=year_id,
                floor=floor_id,
                unit=unit_id,
                address=address,
                nid=nid,
                advance=advance,
                rent_pm=rent_pm,
                date=date,
                branch=branch
            )

            return redirect("rent")

class RentUpdate(View):
    def get(self,request,id):
        rent = Rent.objects.get(id=id)
        form = RentForm(instance=rent)
        floor = Floor.objects.all()
        unit = Unit.objects.all()
        month = Month.objects.all()
        year = Year.objects.all()
        branch = Branch.objects.all()

        context = {
            "form": form,
            "floor": floor,
            "unit": unit,
            "month": month,
            "year": year,
            "branch": branch,
            "rent": rent
        }

        return render(request, "rent/create.html",context)

    def post(self, request,id):
        rent_id = Rent.objects.get(id=id)
        form = RentForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data["address"]
            nid = form.cleaned_data["nid"]
            floor = request.POST["floor"]
            unit = request.POST["unit"]
            advance = form.cleaned_data["advance"]
            rent_pm = form.changed_data["rent_pm"]
            date = form.cleaned_data["date"]
            month = request.POST["month"]
            year = request.POST["year"]
            branch = request.POST["branch"]

            month_id = Month.objects.get(name=month)
            year_id = Year.objects.get(name=year)
            floor_id = Floor.objects.get(floor_no=floor)
            unit_id = Unit.objects.get(unit_no=unit)
            branch_id = Branch.objects.get(name=branch)

            rent_id.address = address
            rent_id.nid = nid
            rent_id.floor=floor_id
            rent_id.unit = unit_id
            rent_id.advance = advance
            rent_id.rent_pm = rent_pm
            rent_id.date = date
            rent_id.month = month_id
            rent_id.year = year_id
            rent_id.branch = branch_id

            rent_id.save()

            return redirect("rent")



def RentDelete(request,id):
    rent = Rent.objects.get(id=id)

    try:
        rent.delete()
        return redirect("rent")
    except Rent.DoesNotExist:
        raise Exception("Rent")

            