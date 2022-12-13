from django.db import models
from apps.utils.models import Timestamp
from apps.floor.models import Floor
from apps.unit.models import Unit
from apps.month.models import Month
from apps.year.models import Year
from apps.branch.models import Branch

# Create your models here.
class Fair(Timestamp):
    type = models.CharField(max_length=100)
    floor = models.OneToOneField(Floor, on_delete=models.CASCADE)
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE)
    rid = models.CharField(max_length=100)
    month = models.OneToOneField(Month, on_delete=models.CASCADE)
    year = models.OneToOneField(Year, on_delete=models.CASCADE)
    water_bill = models.CharField(max_length=100)
    electric_bill = models.DecimalField(max_digits=15, decimal_places=2)
    gas_bill = models.DecimalField(max_digits=15, decimal_places=2)
    security_bill = models.DecimalField(max_digits=15, decimal_places=2)
    utility_bill = models.DecimalField(max_digits=15, decimal_places=2)
    other_bill = models.DecimalField(max_digits=15, decimal_places=2)
    total_rent = models.DecimalField(max_digits=15, decimal_places=2)
    issue_date = models.DateField(null=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

