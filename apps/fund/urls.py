from django.urls import path
from .views import FundList, FundCreate, FundUpdate, FundDelete

urlpatterns = [
    path("", FundList.as_view(), name="fund"),
    path("create/", FundCreate.as_view(), name="fundcreate"),
    path("update/<int:id>", FundUpdate.as_view(), name="fundupdate"),
    path("delete/<int:id>", FundDelete, name="funddelete")
]