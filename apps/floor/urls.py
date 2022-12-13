from django.urls import path
from .views import FloorList, FloorCreate, FloorUpdate, FloorDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        "", login_required(FloorList.as_view(), login_url="/auth/login"), name="floor"
    ),
    path(
        "create/",
        login_required(FloorCreate.as_view(), login_url="/auth/login"),
        name="floorcreate",
    ),
    path(
        "update/<int:id>",
        login_required(FloorUpdate.as_view(), login_url="/auth/login"),
        name="floorupdate",
    ),
    path("delete/<int:id>", FloorDelete, name="floordelete"),
]
