from django.db import models
from apps.utils.models import Timestamp
from apps.floor.models import Floor
from apps.unit.models import Unit
from apps.month.models import Month
from apps.year.models import Year
from apps.branch.models import Branch

# Create your models here.
class Visitor(Timestamp):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    intime = models.DateTimeField()
    outtime = models.DateTimeField()
    month = models.OneToOneField(Year, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
