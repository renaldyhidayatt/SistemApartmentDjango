from django.urls import path
from .views import UnitList, UnitCreate, UnitUpdate, UnitDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(UnitList.as_view(), login_url="/auth/login"), name="unit"),
    path(
        "create",
        login_required(UnitCreate.as_view(), login_url="/auth/login"),
        name="unitcreate",
    ),
    path(
        "update/<int:id>",
        login_required(UnitUpdate.as_view(), login_url="/auth/login"),
        name="unitupdate",
    ),
    path("delete/<int:id>", UnitDelete, name="unitdelete"),
]
