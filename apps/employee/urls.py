from django.urls import path
from .views import EmployeeList, EmployeeCreate, EmployeeUpdate, EmployeeDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        "",
        login_required(EmployeeList.as_view(), login_url="/auth/login"),
        name="employee",
    ),
    path(
        "create/",
        login_required(EmployeeCreate.as_view(), login_url="/auth/login"),
        name="employeecreate",
    ),
    path(
        "update/<int:id>",
        login_required(EmployeeUpdate.as_view(), login_url="/auth/login"),
        name="employeeupdate",
    ),
    path(
        "delete<int:id>",
        EmployeeDelete,
        name="employeedelete",
    ),
]
