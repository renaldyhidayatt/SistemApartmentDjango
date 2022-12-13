from django.urls import path
from .views import MaintanceList, MaintanceCreate, MaintanceUpdate, MaintanceDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        "",
        login_required(MaintanceList.as_view(), login_url="/auth/login"),
        name="maintance",
    ),
    path(
        "create",
        login_required(MaintanceCreate.as_view(), login_url="/auth/login"),
        name="maintancecreate",
    ),
    path(
        "update/<int:id>",
        login_required(MaintanceUpdate.as_view(), login_url="/auth/login"),
        name="maintanceupdate",
    ),
    path("delete/<int:id>", MaintanceDelete, name="maintancedelete"),
]
