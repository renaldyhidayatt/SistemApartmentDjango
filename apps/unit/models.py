from django.db import models
from apps.utils.models import Timestamp
from apps.floor.models import Floor
from apps.branch.models import Branch

# Create your models here.
class Unit(Timestamp):
    floor = models.OneToOneField(Floor, on_delete=models.CASCADE)
    unit_no = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    