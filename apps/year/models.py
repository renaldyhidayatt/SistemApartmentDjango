from django.db import models

from apps.utils.models import Timestamp
# Create your models here.
class Year(Timestamp):
    name = models.CharField(max_length=100)