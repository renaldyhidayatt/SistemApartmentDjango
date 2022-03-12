from django.db import models
from apps.utils.models import Timestamp

# Create your models here.
class Utiliy(Timestamp):
    gas_bill = models.CharField(max_length=100)
    security_bill = models.CharField(max_length=100)
    