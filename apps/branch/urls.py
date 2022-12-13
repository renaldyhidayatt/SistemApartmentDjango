from django.urls import path
from .views import BranchList, BranchCreate, BranchUpdate, BranchDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        "",
        login_required(BranchList.as_view(), login_url="/auth/login"),
        name="branch",
    ),
    path(
        "create/",
        login_required(BranchCreate.as_view(), login_url="/auth/login"),
        name="branchcreate",
    ),
    path(
        "update/<int:id>",
        login_required(BranchUpdate.as_view(), login_url="/auth/login"),
        name="branchupdate",
    ),
    path("delete/<int:id>", BranchDelete, name="branchdelete"),
]
