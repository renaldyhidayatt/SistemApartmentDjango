from django.urls import path
from .views import FairList, FairCreate, FairUpdate, FairDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(FairList.as_view(), login_url="/auth/login"), name="fair"),
    path(
        "create/",
        login_required(FairCreate.as_view(), login_url="/auth/login"),
        name="faircreate",
    ),
    path(
        "update/<int:id>",
        login_required(FairUpdate.as_view(), login_url="/auth/login"),
        name="fairupdate",
    ),
    path("delete/<int:id>", FairDelete, name="fairdelete"),
]
