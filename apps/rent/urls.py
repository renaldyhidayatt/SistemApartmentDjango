from django.urls import path
from .views import RentList, RentCreate, RentUpdate, RentDelete

urlpatterns = [
    path("", RentList.as_view(), name="rent"),
    path("create/", RentCreate.as_view(), name="rentcreate"),
    path("update/<int:id>", RentUpdate.as_view(), name="rentupdate"),
    path("delete/<int:id>", RentList.as_view(), name="rentdelete"),

]