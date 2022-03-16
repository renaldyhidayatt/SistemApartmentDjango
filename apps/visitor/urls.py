from django.urls import path
from .views import VisitorList, VisitorCreate, VisitorUpdate, VisitorDelete

urlpatterns = [
    path("", VisitorList.as_view(),name="visitor"),
    path("create/", VisitorCreate.as_view(),name="visitorcreate"),
    path("update/<int:id>", VisitorUpdate.as_view(),name="visitorupdate"),
    path("delete/<int:id>", VisitorDelete,name="visitordelete"),
]