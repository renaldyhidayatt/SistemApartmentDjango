from django.urls import path
from .views import FloorList, FloorCreate,FloorUpdate, FloorDelete

urlpatterns = [
    path("", FloorList.as_view(), name="floor"),
    path("create/", FloorCreate.as_view(), name="floorcreate"),
    path("update/<int:id>", FloorUpdate.as_view(),name="floorupdate"),
    path("delete/<int:id>", FloorDelete, name="floordelete")
]