from django.urls import path
from .views import BillList, BillCreate, BillUpdate, BillDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", login_required(BillList.as_view(), login_url="/auth/login"), name="bill"),
    path(
        "create/",
        login_required(BillCreate.as_view(), login_url="/auth/login"),
        name="billcreate",
    ),
    path(
        "update/<int:id>",
        login_required(BillUpdate.as_view(), login_url="/auth/login"),
        name="billupdate",
    ),
    path("delete/<int:id>", BillDelete, name="billdelete"),
]
