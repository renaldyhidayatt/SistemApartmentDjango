from django.urls import path
from .views import VisitorList, VisitorCreate, VisitorUpdate, VisitorDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path(
        "",
        login_required(VisitorList.as_view(), login_url="/auth/login"),
        name="visitor",
    ),
    path(
        "create/",
        login_required(VisitorCreate.as_view(), login_url="/auth/login"),
        name="visitorcreate",
    ),
    path(
        "update/<int:id>",
        login_required(VisitorUpdate.as_view(), login_url="/auth/login"),
        name="visitorupdate",
    ),
    path("delete/<int:id>", VisitorDelete, name="visitordelete"),
]
