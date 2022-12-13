from django.db import models
from apps.utils.models import Timestamp
from apps.branch.models import Branch

# Create your models here.
class Floor(Timestamp):
    floor_no = models.CharField(max_length=10)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


    def __str__(self):
        return self.floor_no