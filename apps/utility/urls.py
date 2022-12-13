from django.urls import path
from .views import UtilityList, UtilityCreate, UtilityUpdate, UtilityDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        "",
        login_required(UtilityList.as_view(), login_url="/auth/login"),
        name="utility",
    ),
    path(
        "create/",
        login_required(UtilityCreate.as_view(), login_url="/auth/login"),
        name="utilitycreate",
    ),
    path(
        "update/<int:id>",
        login_required(UtilityUpdate.as_view(), login_url="/auth/login"),
        name="utilityupdate",
    ),
    path("delete/<int:id>", UtilityDelete, name="utilitydelete"),
]
