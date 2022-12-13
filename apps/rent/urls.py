from django.urls import path
from .views import RentList, RentCreate, RentUpdate, RentDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(RentList.as_view(), login_url="/auth/login"), name="rent"),
    path(
        "create/",
        login_required(RentCreate.as_view(), login_url="/auth/login"),
        name="rentcreate",
    ),
    path(
        "update/<int:id>",
        login_required(RentUpdate.as_view(), login_url="/auth/login"),
        name="rentupdate",
    ),
    path("delete/<int:id>", RentDelete, name="rentdelete"),
]
