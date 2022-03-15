from django.urls import path
from .views import BuildingList, BuildingCreate, BuildingUpdate, BuildingDelete

urlpatterns = [
    path("", BuildingList.as_view(), name="building"),
    path("create/", BuildingCreate.as_view(), name="buildingcreate"),
    path("update/<int:id>", BuildingUpdate.as_view(), name="buildingupdate"),
    path("delete/<int:id>", BuildingDelete, name="buildingdelete")
]