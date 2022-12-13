from django.urls import path
from .views import ManagementList, ManagementCreate, ManagementUpdate, ManagementDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        "",
        login_required(ManagementList.as_view(), login_url="/auth/login"),
        name="management",
    ),
    path(
        "create/",
        login_required(ManagementCreate.as_view(), login_url="/auth/login"),
        name="managementcreate",
    ),
    path(
        "update/<int:id>",
        login_required(ManagementUpdate.as_view(), login_url="/auth/login"),
        name="managementupdate",
    ),
    path("delete/<int:id>", ManagementDelete, name="managementdelete"),
]
