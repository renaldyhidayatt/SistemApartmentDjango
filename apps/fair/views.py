from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from .models import Fair
from .forms import FairForm
from apps.month.models import Month
from apps.year.models import Year
from apps.branch.models import Branch
from apps.unit.models import Unit
from apps.floor.models import Floor



# Create your views here.
class FairList(ListView):
    model = Fair
    template_name = "fair/index.html"
    context_object_name = "fair_list"


class FairCreate(View):
    def get(self, request):
        form = FairForm()
        month = Month.objects.all()
        year = Year.objects.all()
        branch = Branch.objects.all()
        unit = Unit.objects.all()
        floor = Floor.objects.all()

        context = {
            "form": form,
            "month": month,
            "year": year,
            "branch": branch,
            "unit": unit,
            "floor": floor
        }

        return render(request,"fair/create.html", context)

    def post(self, request):
        form = FairForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data["type"]
            floor = request.POST["floor"]
            unit = request.POST["unit"]
            rid = form.cleaned_data["rid"]
            month = request.POST["month"]
            year = request.POST["year"]
            water_bill = form.cleaned_data["water_bill"]
            electric_bill = form.cleaned_data["electric_bill"]
            gas_bill = form.cleaned_data["gas_bill"]
            security_bill = form.cleaned_data["security_bill"]
            utility_bill = form.cleaned_data["utility_bill"]
            other_bill = form.cleaned_data["other_bill"]
            total_rent = form.cleaned_data["total_rent"]
            issue_date = form.cleaned_data["issue_date"]
            branch = request.POST["branch"]

            floor_id = Floor.objects.get(floor_no=floor)
            unit_id = Unit.objects.get(unit_no=unit)
            month_id = Month.objects.get(name=month)
            year_id = Year.objects.get(name=year)
            branch_id = Branch.objects.get(name=branch)


            Fair.objects.create(
                type=type,
                floor=floor,
                unit=unit_id,
                rid=rid,
                month=month_id,
                year=year_id,
                water_bill=water_bill,
                electric_bill=electric_bill,
                gas_bill=gas_bill,
                security_bill=security_bill,
                utility_bill=utility_bill,
                other_bill=other_bill,
                total_rent=total_rent,
                issue_date=issue_date,
                branch=branch_id
            )

            return redirect("fair")


class FairUpdate(View):
    def get(self, request, id):
        fair = Fair.objects.get(id=id)
        form = FairForm(instance=fair)
        month = Month.objects.all()
        year = Year.objects.all()
        branch = Branch.objects.all()
        unit = Unit.objects.all()
        floor = Floor.objects.all()

        context = {
            "form": form,
            "month": month,
            "year": year,
            "branch": branch,
            "unit": unit,
            "floor": floor
        }

        return render(request,"fair/update.html", context)

    def post(self, request, id):
        fair = Fair.objects.get(id=id)
        form = FairForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data["type"]
            floor = request.POST["floor"]
            unit = request.POST["unit"]
            rid = form.cleaned_data["rid"]
            month = request.POST["month"]
            year = request.POST["year"]
            water_bill = form.cleaned_data["water_bill"]
            electric_bill = form.cleaned_data["electric_bill"]
            gas_bill = form.cleaned_data["gas_bill"]
            security_bill = form.cleaned_data["security_bill"]
            utility_bill = form.cleaned_data["utility_bill"]
            other_bill = form.cleaned_data["other_bill"]
            total_rent = form.cleaned_data["total_rent"]
            issue_date = form.cleaned_data["issue_date"]
            branch = request.POST["branch"]

            floor_id = Floor.objects.get(floor_no=floor)
            unit_id = Unit.objects.get(unit_no=unit)
            month_id = Month.objects.get(name=month)
            year_id = Year.objects.get(name=year)
            branch_id = Branch.objects.get(name=branch)

            fair.type = type
            fair.floor = floor_id
            fair.unit = unit_id
            fair.rid = rid
            fair.month = month_id
            fair.year = year_id
            fair.water_bill = water_bill
            fair.electric_bill = electric_bill
            fair.security_bill = security_bill
            fair.utility_bill = utility_bill
            fair.other_bill = other_bill
            fair.total_rent = total_rent
            fair.issue_date = issue_date
            fair.branch = branch_id

            return redirect("fair")



def FairDelete(request, id):
    fair = Fair.objects.get(id=id)
    try:
        fair.delete()
        return redirect("fair")
    except Fair.DoesNotExist:
        raise Exception("Bisa")