from django.db import models
from apps.utils.models import Timestamp
from apps.branch.models import Branch

# Create your models here.
class BuildingInfo(Timestamp):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    securityGuardMobile = models.CharField(max_length=200)
    secratatyMobile = models.CharField(max_length=200)
    moderatorMobile = models.CharField(max_length=200)
    buildingMakeYear = models.CharField(max_length=200)
    b_name = models.CharField(max_length=200)
    b_address = models.CharField(max_length=200)
    b_phone = models.CharField(max_length=200)
    buildingImage = models.ImageField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    