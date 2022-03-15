from django.urls import path
from .views import FairList, FairCreate, FairUpdate, FairDelete

urlpatterns = [
    path("", FairList.as_view(), name="fair"),
    path("create/", FairCreate.as_view(), name="faircreate"),
    path("update/<int:id>", FairUpdate.as_view(), name="fairupdate"),
    path("delete/<int:id>", FairDelete, name="fairdelete")
]