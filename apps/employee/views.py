from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Employee, EmployeeSalary
from .forms import EmployeeForm, EmployeeSalaryForm
from apps.users.models import Users
from apps.branch.models import Branch
from apps.year.models import Year
from apps.month.models import Month
from apps.users.models import Users
from django.contrib import messages


# Create your views here.
class EmployeeList(LoginRequiredMixin, ListView):
    model = Employee
    template_name = "employee/index.html"
    context_object_name = "employee_list"


class EmployeeSalaryList(LoginRequiredMixin, ListView):
    model = EmployeeSalary
    template_name = "employeesalary/index.html"
    context_object_name = "em_salarylist"


class EmployeeCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = EmployeeForm()
        user = Users.objects.all()
        branch = Branch.objects.all()

        context = {"form": form, "user": user, "branch": branch}

        return render(request, "employee/create.html", context)

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data["address"]
            nid = form.cleaned_data["nid"]
            designation = form.cleaned_data["designation"]
            date = form.cleaned_data["date"]
            ending_date = form.cleaned_data["ending_date"]
            user = form.cleaned_data["user"]
            branch = form.cleaned_data["branch"]

            user_id = Users.objects.filter(is_superuser=False, email=user)
            branch_id = Branch.objects.get(name=branch)

            Employee.objects.create(
                address=address,
                nid=nid,
                designation=designation,
                date=date,
                ending_date=ending_date,
                user=user_id,
                branch=branch_id,
            )
            messages.success(request, "berhasil membuat employee")
            return redirect("employee")
        else:
            messages.error(request, "gagal membuat employee")
            return redirect("employee")


class EmployeSalaCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = EmployeeSalaryForm()
        year = Year.objects.all()
        month = Month.objects.all()
        employee = Employee.objects.all()

        context = {"form": form, "year": year, "month": month, "employee": employee}

        return render(request, "employesalary/create.html", context)

    def post(self, request):
        form = EmployeeSalaryForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data["amount"]
            year = request.POST["year"]
            month = request.POST["month"]
            employee = request.POST["employee"]

            year_id = Year.objects.get(name=year)
            month_id = Month.objects.get(name=month)
            employee_id = Employee.objects.get(user__name=employee)

            EmployeeSalary.objects.create(
                amount=amount, year=year_id, month=month_id, employee=employee_id
            )
            messages.success(request, "Berhasil membuat employee")

            return redirect("employeesalary")
        else:
            messages.error(request, "Gagal membuat employee")
            return redirect("employeesalary")


class EmployeeUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        employee = Employee.objects.get(id=id)
        form = EmployeeForm(instance=employee)
        user = Users.objects.all()
        branch = Branch.objects.all()

        context = {"form": form, "user": user, "branch": branch, "employee": employee}

        return render(request, "employesalary/update.html", context)

    def post(self, request, id):
        form = EmployeeForm(request.POST)
        employee = Employee.objects.get(id=id)
        if form.is_valid():
            address = form.cleaned_data["address"]
            nid = form.cleaned_data["nid"]
            designation = form.cleaned_data["designation"]
            date = form.cleaned_data["date"]
            ending_date = form.cleaned_data["ending_date"]
            user = form.cleaned_data["user"]
            branch = form.cleaned_data["branch"]

            user_id = Users.objects.get(email=user)
            branch_id = Branch.objects.get(name=branch)

            employee.address = address
            employee.nid = nid
            employee.designation = designation
            employee.date = date
            employee.ending_date = ending_date
            employee.user = user_id
            employee.branch = branch_id

            employee.save()
            messages.success(request, "Berhasil update employee")
            return redirect("employee")
        else:
            messages.error(request, "Gagal update employee")
            return redirect("employee")


class EmployeSalaUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        form = EmployeeSalaryForm()
        year = Year.objects.all()
        month = Month.objects.all()
        employee = Employee.objects.all()

        context = {"form": form, "year": year, "month": month, "employee": employee}

        return render(request, "employesalary/update.html", context)

    def post(self, request, id):
        employesala = EmployeeSalary.objects.get(id=id)
        form = EmployeeSalaryForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data["amount"]
            year = request.POST["year"]
            month = request.POST["month"]
            employee = request.POST["employee"]

            year_id = Year.objects.get(name=year)
            month_id = Month.objects.get(name=month)
            employee_id = Employee.objects.get(user__name=employee)

            employesala.amount = amount
            employesala.year = year_id
            employesala.month = month_id
            employesala.employee = employee_id

            employesala.save()
            messages.success(request, "Berhasil update employee salery")
            return redirect("employeesalary")
        else:
            messages.error(request, "Gagal update employee salery")
            return redirect("employeesalary")


@login_required(login_url="/auth/login")
def EmployeeDelete(request, id):
    employee = Employee.objects.get(id=id)

    try:
        employee.delete()
        messages.success(request, "Berhasil delete employee")
        return redirect("employee")
    except Employee.DoesNotExist:
        messages.error(request, "Gagal delete employee")
        return redirect("employee")


@login_required(login_url="/auth/login")
def EmployeeSalaDelete(request):
    employesala = EmployeeSalary.objects.get(id=id)
    try:
        employesala.delete()
        messages.success(request, "Berhasil delete employee salery")
        return redirect("employeesalary")
    except EmployeeSalary.DoesNotExist:
        messages.error(request, "Gagal delete employee salery")
        return redirect("employeesalary")
