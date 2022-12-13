from django.urls import path
from .views import FundList, FundCreate, FundUpdate, FundDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(FundList.as_view(), login_url="/auth/login"), name="fund"),
    path(
        "create/",
        login_required(FundCreate.as_view(), login_url="/auth/login"),
        name="fundcreate",
    ),
    path(
        "update/<int:id>",
        login_required(FundUpdate.as_view(), login_url="/auth/login"),
        name="fundupdate",
    ),
    path("delete/<int:id>", FundDelete, name="funddelete"),
]
