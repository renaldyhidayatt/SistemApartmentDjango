from django.shortcuts import render

# from django.db.models import Sum
from apps.rent.models import Rent
from apps.maintenace.models import Maintance
from apps.fair.models import Fair
from apps.management.models import Management
from django.contrib.auth.decorators import login_required


@login_required(login_url="/auth/login")
def DashboardView(request):
    rent_count = Rent.objects.count()
    maintance_count = Maintance.objects.count()
    fair_count = Fair.objects.count()
    management_count = Management.objects.count()

    context = {
        "rent_count": rent_count,
        "maintance_count": maintance_count,
        "fair_count": fair_count,
        "management_count": management_count,
    }

    return render(request, "index.html", context)
