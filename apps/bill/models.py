from django.db import models
from apps.utils.models import Timestamp
from django.utils.timezone import now
from apps.month.models import Month
from apps.year.models import Year
from apps.branch.models import Branch

# Create your models here.
class Bill(Timestamp):
    type = models.CharField(
        "Bill Type",
        max_length=100,
        error_messages={"max_length": "You cant add more than 100 characters"},
    )
    date = models.DateField(default=now)
    month = models.OneToOneField(Month, on_delete=models.CASCADE)
    year = models.OneToOneField(Year, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=15,decimal_places=2)
    deposit_bank = models.CharField(
        max_length=200,
        error_messages={"max_length": "You cant add more than 200 characters"},
    )
    details = models.CharField(
        max_length=200,
        error_messages={"max_length": "You cant add more than 200 characters"},
    )
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "All Bill"
        verbose_name_plural = "Alll Bills"        



class BillType(Timestamp):
    bill_type = models.CharField(max_length=200, error_messages={"max_length": "You cant add more than 200 characters"})


    