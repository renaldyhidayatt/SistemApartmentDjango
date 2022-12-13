from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Management
from .forms import ManagementForm
from apps.branch.models import Branch
from django.contrib import messages

# Create your views here.
class ManagementList(LoginRequiredMixin, ListView):
    model = Management
    template_name = "management/index.html"
    context_object_name = "management_list"


class ManagementCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = ManagementForm()
        branch = Branch.objects.all()
        context = {"form": form, "branch": branch}
        return render(request, "management/create.html", context)

    def post(self, request):
        form = ManagementForm(request.POST)
        if form.is_valid():
            contact = form.cleaned_data["contact"]
            address = form.cleaned_data["address"]
            nid = form.cleaned_data["nid"]
            member_type = form.cleaned_data["member_type"]
            joining_date = form.cleaned_data["joining_date"]
            status = form.cleaned_data["status"]
            branch = request.POST["branch"]

            branch_id = Branch.objects.get(name=branch)

            Management.objects.create(
                contact=contact,
                address=address,
                nid=nid,
                member_type=member_type,
                joining_date=joining_date,
                status=status,
                branch=branch_id,
            )
            messages.success(request, "Berhasil membuat management")

            return redirect("management")
        else:
            messages.error(request, "Gagal create management")
            return redirect("management")


class ManagementUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        management = Management.objects.get(id=id)
        form = ManagementForm(instance=management)
        branch = Branch.objects.all()
        context = {"form": form, "branch": branch}
        return render(request, "management/create.html", context)

    def post(self, request, id):
        management = Management.objects.get(id=id)
        form = ManagementForm(request.POST)
        if form.is_valid():
            contact = form.cleaned_data["contact"]
            address = form.cleaned_data["address"]
            nid = form.cleaned_data["nid"]
            member_type = form.cleaned_data["member_type"]
            joining_date = form.cleaned_data["joining_date"]
            status = form.cleaned_data["status"]
            branch = request.POST["branch"]

            branch_id = Branch.objects.get(name=branch)

            management.contact = contact
            management.address = address
            management.nid = nid
            management.member_type = member_type
            management.joining_date = joining_date
            management.status = status
            management.branch = branch_id

            management.save()

            messages.success(request, "Berhasil update management")

            return redirect("management")
        else:
            messages.error(request, "Gagal update management")

            return redirect("management")


@login_required(login_url="/auth/login")
def ManagementDelete(request, id):
    management = Management.objects.get(id=id)
    try:
        management.delete()
        messages.success(request, "Berhasil delete management")
        return redirect("management")

    except Management.DoesNotExist:
        messages.error(request, "Gagal update management")
        return redirect("management")
