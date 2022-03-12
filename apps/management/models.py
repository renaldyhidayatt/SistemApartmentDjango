from django.db import models
from apps.utils.models import Timestamp
from apps.branch.models import Branch
from django.utils.timezone import now

# Create your models here.
class Management(Timestamp):
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    member_type = models.CharField(max_length=100)
    joining_date = models.DateField(default=now)
    end_date = models.DateField(null=True)
    status = models.IntegerField(default=0)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)