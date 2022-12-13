from django.db import models
from apps.utils.models import Timestamp

# Create your models here.
class Branch(Timestamp):
    name = models.CharField(
        max_length=100,
        error_messages={"max_length": "You cant add more than 100 characters"},
    )
    email = models.CharField(
        max_length=50,
        error_messages={"max_length": "You cant add more than 50 characters"},
    )
    contact = models.IntegerField()
    address = models.CharField(
        max_length=100,
        error_messages={"max_length": "You cant add more than 100 characters"},
    )
    status = models.CharField(
        max_length=50,
        error_messages={"max_length": "You cant add more than 50 characters"},
    )
