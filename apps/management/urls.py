from django.urls import path
from .views import ManagementList, ManagementCreate, ManagementUpdate, ManagementDelete

urlpatterns = [
    path("",ManagementList.as_view(),name="management"),
    path("create/",ManagementCreate.as_view(),name="managementcreate"),
    path("update/<int:id>",ManagementUpdate.as_view(),name="managementupdate"),
    path("delete/<int:id>",ManagementDelete,name="managementdelete"),
]