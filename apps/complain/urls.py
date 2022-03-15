from django.urls import path
from .views import ComplainList, ComplainCreate, ComplainUpdate, ComplainDelete

urlpatterns= [
    path("", ComplainList.as_view(),name="complain"),
    path("create/", ComplainCreate.as_view(), name="complaincreate"),
    path("update/<int:id>", ComplainUpdate.as_view(), name="complainupdate"),
    path("delete/<int:id>", ComplainDelete,name="complaindelete")
]