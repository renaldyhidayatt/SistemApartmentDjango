from django.urls import path
from .views import MaintanceList, MaintanceCreate, MaintanceUpdate, MaintanceDelete

urlpatterns = [
    path("", MaintanceList.as_view(), name="maintance"),
    path("create", MaintanceCreate.as_view(), name="maintancecreate"),
    path("update/<int:id>", MaintanceUpdate.as_view(), name="maintanceupdate"),
    path("delete/<int:id>", MaintanceDelete, name="maintancedelete"),

    
]