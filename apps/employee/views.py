from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from .models import Employee, EmployeeSalary
from .forms import EmployeeForm, EmployeeSalaryForm
from apps.users.models import Users
from apps.branch.models import Branch
from apps.year.models import Year
from apps.month.models import Month


# Create your views here.
class EmployeeList(ListView):
    model = Employee
    template_name = "employee/index.html"
    context_object_name = "employee_list"


class EmployeeSalaryList(ListView):
    model = EmployeeSalary
    template_name = "employeesalary/index.html"
    context_object_name = "em_salarylist"


class EmployeeCreate(View):
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

            user_id = User.objects.get(email=user)
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

            return redirect("employee")


class EmployeSalaCreate(View):
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

            return redirect("employeesalary")


class EmployeeUpdate(View):
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

            user_id = User.objects.get(email=user)
            branch_id = Branch.objects.get(name=branch)

            employee.address = address
            employee.nid = nid
            employee.designation = designation
            employee.date = date
            employee.ending_date =ending_date
            employee.user = user_id
            employee.branch = branch_id

            employee.save()

            return redirect("employee")


class EmployeSalaUpdate(View):
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

            return redirect("employeesalary")



def EmployeeDelete(request, id):
    employee = Employee.objects.get(id=id)

    try:
        employee.delete()
        return redirect("employee")
    except Employee.DoesNotExist:
        raise Exception("Employee")


def EmployeeSalaDelete(request):
    employesala = EmployeeSalary.objects.get(id=id)
    try:
        employesala.delete()
        return redirect("employee")
    except EmployeeSalary.DoesNotExist:
        raise Exception("Employee")
