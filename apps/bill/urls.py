from django.urls import path
from .views import BillList, BillCreate, BillUpdate, BillDelete


urlpatterns = [
    path("", BillList.as_view(), name="bill"),
    path("create/", BillCreate.as_view(), name="billcreate"),
    path("update/<int:id>",BillUpdate.as_view(), name="billupdate"),
    path("delete/<int:id>", BillDelete, name="billdelete")
]