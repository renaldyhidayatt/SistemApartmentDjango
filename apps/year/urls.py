from django.urls import path
from .views import YearList, YearCreate, YearUpdate,YearDelete

urlpatterns = [
    path("", YearList.as_view(),name="year"),
    path("create/", YearCreate.as_view(),name="yearcreate"),
    path("update/<int:id>", YearUpdate.as_view(),name="yearupdate"),
    path("delete/<int:id>", YearDelete,name="yeardelete"),
]