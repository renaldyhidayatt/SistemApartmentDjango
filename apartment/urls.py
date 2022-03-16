"""apartment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("bill/", include("apps.bill.urls")),
    path("branch/", include("apps.branch.urls")),
    path("building/", include("apps.building.urls")),
    path("complain/", include("apps.complain.urls")),
    path("employee/", include("apps.employee.urls")),
    path("fair/", include("apps.fair.urls")),
    path("floor/", include("apps.floor.urls")),
    path("fund/", include("apps.fund.urls")),
    path("maintance/", include("apps.maintenace.urls")),
    path("management/", include("apps.management.urls")),
    path("month/", include("apps.month.urls")),
    path("rent/", include("apps.rent.urls")),
    path("unit/", include("apps.unit.urls")),
    path("visitor/", include("apps.visitor.urls")),
    path("year/", include("apps.year.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
