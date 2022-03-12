from django.db import models
from apps.utils.models import Timestamp
from apps.users.models import Users

# Create your models here.
class Role(Timestamp):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    