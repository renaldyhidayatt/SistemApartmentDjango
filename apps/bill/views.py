from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DeleteView
from .forms import BillForm
from .models import Bill
from apps.month.models import Month
from apps.year.models import Year
from apps.branch.models import Branch
from django.shortcuts import get_object_or_404


# Create your views here.
class BillList(ListView):
    model = Bill
    template_name = "bill/index.html"
    context_object_name = "bill_list"

class BillCreate(View):
    def get(self, request):
        month = Month.objects.all()
        year = Year.objects.all()
        branch = Branch.objects.all()
        
        bill = Bill.objects.get(id=id)

        

        form = BillForm()
        context = {
            "form": form,
            "bill": bill,
            "month": month,
            "year": year,
            "branch": branch
        }

        return render(request, "bill/update.html", context)
       

    def post(self, request):
        if self.form_classes.is_valid():
            type = form.cleaned_data["type"]
            date = form.cleaned_data["date"]
            deposit_bank = form.cleaned_data["deposit_bank"]
            details = form.cleaned_data["details"]
            month = request.POST["month"]
            year = request.POST["year"]
            branch = request.POST["branch"]

            month_name = Month.objects.get(name=month)
            year_name = Year.objects.get(name=year)
            branch_name = Branch.objects.get(name=branch)

            Bill.objects.create(
                type=type,
                date=date,
                deposit_bank=deposit_bank,
                details=details,
                month=month_name,
                year=year_name,
                branch=branch_name
            )

            return redirect("bill")


class BillUpdate(View):
    
    def get(self, request, id):
        month = Month.objects.all()
        year = Year.objects.all()
        branch = Branch.objects.all()
        
        bill = Bill.objects.get(id=id)

        

        form = BillForm(instance=bill)
        context = {
            "form": form,
            "bill": bill,
            "month": month,
            "year": year,
            "branch": branch
        }

        return render(request, "bill/update.html", context)
        

    def post(self, request, id):
        bill = Bill.objects.get(id=id)
        form = BillForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data["type"]
            date = form.cleaned_data["date"]
            deposit_bank = form.cleaned_data["deposit_bank"]
            details = form.cleaned_data["details"]
            month = request.POST["month"]
            year = request.POST["year"]
            branch = request.POST["branch"]

            month_name = Month.objects.get(name=month)
            year_name = Year.objects.get(name=year)
            branch_name = Branch.objects.get(name=branch)

            bill.type = type
            bill.date = date
            bill.deposit_bank = deposit_bank
            bill.details = details
            bill.month = month_name
            bill.year = year_name
            bill.branch = branch_name

            bill.save()

            return redirect('bill')






def BillDelete(request, id):
    bill = Bill.objects.get(id=id)

    try:
        bill.delete()
    except Bill.DoesNotExist:
        raise Exception("Nice")
    
