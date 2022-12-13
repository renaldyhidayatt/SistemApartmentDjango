from django.urls import path
from .views import YearList, YearCreate, YearUpdate, YearDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(YearList.as_view(), login_url="/auth/login"), name="year"),
    path(
        "create/",
        login_required(YearCreate.as_view(), login_url="/auth/login"),
        name="yearcreate",
    ),
    path(
        "update/<int:id>",
        login_required(YearUpdate.as_view(), login_url="/auth/login"),
        name="yearupdate",
    ),
    path(
        "delete/<int:id>",
        YearDelete,
        name="yeardelete",
    ),
]
