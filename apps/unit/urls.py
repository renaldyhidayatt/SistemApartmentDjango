from django.urls import path
from .views import UnitList, UnitCreate, UnitUpdate, UnitDelete

urlpatterns = [
    path("", UnitList.as_view(), name="unit"),
    path("create", UnitCreate.as_view(), name="unitcreate"),
    path("update/<int:id>", UnitUpdate.as_view(), name="unitupdate"),
    path("delete/<int:id>", UnitDelete, name="unitdelete"),
]