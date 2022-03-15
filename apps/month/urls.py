from django.urls import path
from .views import MonthList, MonthCreate, MonthUpdate, MonthDelete

urlpatterns = [
    path("", MonthList.as_view(), name="month"),
    path("create/", MonthCreate.as_view(), name="monthcreate"),
    path("update/<int:id>", MonthUpdate.as_view(), name="monthupdate"),
    path("delete/<int:id>", MonthDelete, name="monthdelete"),
]