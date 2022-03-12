from django.db import models
from apps.utils.models import Timestamp
from django.utils.timezone import now
from apps.branch.models import Branch
from apps.users.models import Users
from apps.month.models import Month
from apps.year.models import Year

# Create your models here.
class Employee(Timestamp):
    address = models.CharField(max_length=100)
    nid = models.CharField(max_length=200)
    designation = models.IntegerField()
    date = models.DateField(default=now)
    ending_date = models.DateField(null=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


    def __str__(self):
        return self.nid


class EmployeeSalary(Timestamp):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.OneToOneField(Year, on_delete=models.CASCADE)
    month = models.OneToOneField(Month, on_delete=models.CASCADE)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee.user.email