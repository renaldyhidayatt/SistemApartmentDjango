from django.db import models
from apps.utils.models import Timestamp
from apps.month.models import Month
from apps.year.models import Year

# Create your models here.
class Maintance(Timestamp):
    title = models.CharField(max_length=100)
    date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    details = models.TextField()
    month = models.OneToOneField(Month, on_delete=models.CASCADE)
    year = models.OneToOneField(Year, on_delete=models.CASCADE)
    