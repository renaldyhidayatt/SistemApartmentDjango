from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Floor
from .forms import FloorForm
from apps.branch.models import Branch
from django.contrib import messages

# Create your views here.


class FloorList(LoginRequiredMixin, ListView):
    model = Floor
    template_name = "floor/index.html"
    context_object_name = "floor_list"


class FloorCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = FloorForm()
        branch = Branch.objects.all()

        context = {"form": form, "branch": branch}

        return render(request, "floor/create.html", context)

    def post(self, request):
        form = FloorForm(request.POST)
        if form.is_valid():
            floor_no = form.cleaned_data["floor_no"]
            branch = request.POST["branch"]

            branch_id = Branch.objects.get(name=branch)

            Floor.objects.create(floor_no=floor_no, branch=branch_id)
            messages.success(request, "Berhasil membuat floor")

            return redirect("floor")
        else:
            messages.error(request, "Gagal membuat floor")
            return redirect("floor")


class FloorUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        floor = Floor.objects.get(id=id)
        form = FloorForm(instance=floor)
        branch = Branch.objects.all()

        context = {"form": form, "branch": branch, "floor": floor}

        return render(request, "floor/update.html", context)

    def post(self, request, id):
        floor = Floor.objects.get(id=id)
        form = FloorForm(request.POST)

        if form.is_valid():
            floor_no = form.cleaned_data["floor_no"]
            branch = request.POST["branch"]

            branch_id = Branch.objects.get(name=branch)

            floor.floor_no = floor_no
            floor.branch = branch_id

            floor.save()

            messages.success(request, "Berhasil update floor")
            return redirect("floor")
        else:
            messages.error(request, "Gagal update floor")
            return redirect("floor")


@login_required(login_url="/auth/login")
def FloorDelete(request, id):
    floor = Floor.objects.get(id=id)

    try:
        floor.delete()
        messages.success(request, "Berhasil delete floor")
        return redirect("floor")
    except Floor.DoesNotExist:
        messages.error(request, "Gagal delete floor")
        return redirect("floor")
