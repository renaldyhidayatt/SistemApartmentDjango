from django.urls import path
from .views import BranchList, BranchCreate, BranchUpdate, BranchDelete

urlpatterns = [
    path("", BranchList.as_view(), name="branch"),
    path("create/", BranchCreate.as_view(), name="branchcreate"),
    path("update/<int:id>", BranchUpdate.as_view(), name="branchupdate"),
    path("delete/<int:id>", BranchDelete, name="branchdelete")
]