from django.urls import path
from .views import BuildingList, BuildingCreate, BuildingUpdate, BuildingDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        "",
        login_required(BuildingList.as_view(), login_url="/auth/login"),
        name="building",
    ),
    path(
        "create/",
        login_required(BuildingCreate.as_view(), login_url="/auth/login"),
        name="buildingcreate",
    ),
    path(
        "update/<int:id>",
        login_required(BuildingUpdate.as_view(), login_url="/auth/login"),
        name="buildingupdate",
    ),
    path("delete/<int:id>", BuildingDelete, name="buildingdelete"),
]
