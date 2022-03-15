from django.urls import path
from .views import UtilityList, UtilityCreate, UtilityUpdate, UtilityDelete

urlpatterns = [
    path('', UtilityList.as_view(), name="utility"),
    path('create/', UtilityCreate.as_view(), name="utilitycreate"),
    path('update/<int:id>', UtilityUpdate.as_view(), name="utilityupdate"),
    path('delete/<int:id>', UtilityDelete, name="utilitydelete"),
]