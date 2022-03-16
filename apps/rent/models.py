from django.db import models
from apps.utils.models import Timestamp
from apps.floor.models import Floor
from django.utils.timezone import now
from apps.month.models import Month
from apps.year.models import Year
from apps.branch.models import Branch
from apps.unit.models import Unit

# Create your models here.
class Rent(Timestamp):
    address = models.CharField(max_length=200)
    nid = models.CharField(max_length=200)
    floor = models.OneToOneField(Floor, on_delete=models.CASCADE)
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE)
    advance = models.DecimalField(max_digits=15, decimal_places=2)
    rent_pm = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(default=now)
    month = models.OneToOneField(Month, on_delete=models.CASCADE)
    year = models.OneToOneField(Year, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


    def __str__(self):
        return self.address