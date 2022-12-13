from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import BillForm
from .models import Bill
from apps.month.models import Month
from apps.year.models import Year
from apps.branch.models import Branch
from django.contrib import messages


# Create your views here.
class BillList(LoginRequiredMixin, ListView):
    model = Bill
    template_name = "bill/index.html"
    context_object_name = "bill_list"


class BillCreate(LoginRequiredMixin, View):
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
            "branch": branch,
        }

        return render(request, "bill/update.html", context)

    def post(self, request):
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

            Bill.objects.create(
                type=type,
                date=date,
                deposit_bank=deposit_bank,
                details=details,
                month=month_name,
                year=year_name,
                branch=branch_name,
            )
            messages.success(request, "Berhasil membuat bill")

            return redirect("bill")
        else:
            messages.error(request, "Failed create bill")
            return redirect("bill")


class BillUpdate(LoginRequiredMixin, View):
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
            "branch": branch,
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
            messages.success(request, "Berhasil update bill")
            return redirect("bill")
        else:
            messages.error(request, "Gagal update bill")
            return redirect("bill")


@login_required(login_url="/auth/login")
def BillDelete(request, id):
    bill = Bill.objects.get(id=id)

    try:
        bill.delete()
        messages.success(request, "Berhasil hapus bill")
        return redirect("bill")
    except Bill.DoesNotExist:
        messages.error(request, "Gagal delete bill")
        return redirect("bill")
