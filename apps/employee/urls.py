from django.urls import path
from .views import EmployeeList, EmployeeCreate, EmployeeUpdate, EmployeeDelete

urlpatterns = [
    path("", EmployeeList.as_view(),name="employee"),
    path("create/", EmployeeCreate.as_view(),name="employeecreate"),
    path("update/<int:id>", EmployeeUpdate.as_view(),name="employeeupdate"),
    path("delete<int:id>", EmployeeDelete, name="employeedelete")
]
