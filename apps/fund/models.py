from django.db import models
from apps.utils.models import Timestamp
from apps.month.models import Month
from apps.year.models import Year
from apps.branch.models import Branch

# Create your models here.
class Fund(Timestamp):
    month = models.OneToOneField(Month, on_delete=models.CASCADE)
    year = models.OneToOneField(Year, on_delete=models.CASCADE)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=15, decimal_places=2)
    purpose = models.CharField(max_length=200)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
