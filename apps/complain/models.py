from django.db import models
from apps.utils.models import Timestamp
from apps.month.models import Month
from apps.year.models import Year
from apps.users.models import Users

# Create your models here.
class Complain(Timestamp):
    title = models.CharField(
        max_length=100,
        error_messages={"max_length": "You cant add more than 100 characters"},
    )
    description = models.CharField(
        max_length=100,
        error_messages={"max_length": "You cant add more than 100 characters"},
    )
    date = models.CharField(
        max_length=100,
        error_messages={"max_length": "You cant add more than 100 characters"},
    )
    month = models.OneToOneField(Month, on_delete=models.CASCADE)
    year = models.OneToOneField(Year, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    
