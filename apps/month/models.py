from django.db import models
from apps.utils.models import Timestamp

# Create your models here.
class Month(Timestamp):
    name = models.CharField(max_length=100)