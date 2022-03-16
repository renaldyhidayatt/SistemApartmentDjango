from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import Fund
from apps.month.models import Month
from apps.year.models import Year
from apps.branch.models import Branch
from .forms import FundForm


# Create your views here.
class FundList(ListView):
    model = Fund
    template_name = "fund/index.html"
    context_object_name = "fund_list"


class FundCreate(View):
    def get(self, request):
        form = FundForm()
        month = Month.objects.all()
        year = Year.objects.all()
        branch = Branch.objects.all()

        context = {
            "form": form,
            "month": month,
            "year": year,
            "branch": branch
        }

        return render(request, "fund/create.html", context)

    def post(self, request):
        form = FundForm(request.POST)
        if form.is_valid():
            date= form.cleaned_data["date"]
            total_amount = form.cleaned_data["total_amount"]
            purpose = form.cleaned_data["purpose"]
            month = request.POST["month"]
            year = request.POST["year"]
            branch = request.POST["branch"]

            month_id = Month.objects.get(name=month)
            year_id = Year.objects.get(name=year)
            branch_id = Branch.objects.get(name=branch)

            Fund.objects.create(
                date=date,
                total_amount=total_amount,
                purpose=purpose,
                month=month_id,
                year=year_id,
                branch=branch_id
            )

            return redirect("fund")



class FundUpdate(View):
    def get(self, request, id):
        fund = Fund.objects.get(id=id)
        form = FundForm(instance=fund)

        month = Month.objects.all()
        year = Year.objects.all()
        branch = Branch.objects.all()

        context = {
            "form": form,
            "month": month,
            "year": year,
            "branch": branch,
            "fund": fund
        }

        return render(request, "fund/update.html", context)


    def post(self, request, id):
        fund = Fund.objects.get(id=id)
        form = FundForm(request.POST)
        if form.is_valid():
            date= form.cleaned_data["date"]
            total_amount = form.cleaned_data["total_amount"]
            purpose = form.cleaned_data["purpose"]
            month = request.POST["month"]
            year = request.POST["year"]
            branch = request.POST["branch"]

            month_id = Month.objects.get(name=month)
            year_id = Year.objects.get(name=year)
            branch_id = Branch.objects.get(name=branch)

            fund.date = date
            fund.total_amount = total_amount
            fund.purpose = purpose
            fund.month = month_id
            fund.year = year
            fund.branch = branch_id

            fund.delete()

            return redirect("fund")


def FundDelete(request, id):
    fund = Fund.objects.get(id=id)

    try:
        fund.delete()
        return redirect("fund")
    except Fund.DoesNotExist:
        raise Exception("Error")