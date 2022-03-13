from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import Management
from .forms import ManagementForm
from apps.branch.models import Branch

# Create your views here.
class ManagementList(ListView):
    model = Management
    template_name = "management/index.html"
    context_object_name = "management_list"


class ManagementCreate(View):
    def get(self, request):
        form = ManagementForm()
        branch = Branch.objects.all()
        context = {
            "form": form,
            "branch": branch
        }
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
                branch=branch_id
            )

            return redirect("management")

class ManagementUpdate(View):
    def get(self, request,id):
        management = Management.objects.get(id=id)
        form = ManagementForm(instance=management)
        branch = Branch.objects.all()
        context = {
            "form": form,
            "branch": branch
        }
        return render(request, "management/create.html", context)

    def post(self, request,id):
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


            return redirect("management")


def ManagementDelete(request,id):
    management = Management.objects.get(id=id)
    try:
        management.delete()
        return redirect("management")

    except Management.DoesNotExist:
        raise Exception("No")