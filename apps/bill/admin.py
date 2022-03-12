from django.contrib import admin
from .models import Bill, BillType

# Register your models here.
admin.site.register(Bill)
admin.site.register(BillType)