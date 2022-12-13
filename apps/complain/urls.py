from django.urls import path
from .views import ComplainList, ComplainCreate, ComplainUpdate, ComplainDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        "",
        login_required(ComplainList.as_view(), login_url="/auth/login"),
        name="complain",
    ),
    path(
        "create/",
        login_required(ComplainCreate.as_view(), login_url="/auth/login"),
        name="complaincreate",
    ),
    path(
        "update/<int:id>",
        login_required(ComplainUpdate.as_view(), login_url="/auth/login"),
        name="complainupdate",
    ),
    path("delete/<int:id>", ComplainDelete, name="complaindelete"),
]
