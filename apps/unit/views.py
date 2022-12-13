from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .forms import UnitForm
from .models import Unit
from apps.branch.models import Branch
from apps.floor.models import Floor
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
class UnitList(LoginRequiredMixin, ListView):
    model = Unit
    template_name = "unit/index.html"
    context_object_name = "unit_list"


class UnitCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = UnitForm()
        branch = Branch.objects.all()
        floor = Floor.objects.all()

        context = {"form": form, "branch": branch, "floor": floor}

        return render(request, "unit/create.html", context)

    def post(self, request):
        form = UnitForm(request.POST)
        if form.is_valid():
            floor = request.POST["floor"]
            unit_no = form.cleaned_data["unit_no"]
            branch = request.POST["branch"]

            floor_id = Floor.objects.get(floor_no=floor)
            branch_id = Branch.objects.get(name=branch)

            Unit.objects.create(floor=floor_id, unit_no=unit_no, branch=branch_id)

            messages.success(request, "Berhasil membuat unit")

            return redirect("unit")
        else:
            messages.error(request, "Gagal create unit")
            return redirect("unit")


class UnitUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        unit_id = Unit.objects.get(id=id)
        form = UnitForm(instance=unit_id)
        branch = Branch.objects.all()
        floor = Floor.objects.all()

        context = {"form": form, "branch": branch, "floor": floor, "unit": unit_id}

        return render(request, "unit/create.html", context)

    def post(self, request, id):
        unit_id = Unit.objects.get(id=id)
        form = UnitForm(request.POST)
        if form.is_valid():
            floor = request.POST["floor"]
            unit_no = form.cleaned_data["unit_no"]
            branch = request.POST["branch"]

            floor_id = Floor.objects.get(floor_no=floor)
            branch_id = Branch.objects.get(name=branch)

            unit_id.floor = floor_id
            unit_id.branch = branch_id
            unit_id.unit_no = unit_no

            messages.success(request, "Berhasil update unit")

            return redirect("unit")
        else:
            messages.error(request, "Gagal update unit")
            return redirect("unit")


@login_required(login_url="/auth/login")
def UnitDelete(request, id):
    unit_id = Unit.objects.get(id=id)
    try:
        unit_id.delete()
        messages.success(request, "Berhasil delete unit")

        return redirect("unit")
    except Unit.DoesNotExist:
        messages.error(request, "Gagal delete unit")
        return redirect("unit")
