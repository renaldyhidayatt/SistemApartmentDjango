from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import BranchForm
from .models import Branch
from django.contrib import messages


# Create your views here.
class BranchList(LoginRequiredMixin, ListView):
    model = Branch
    template_name = "branch/index.html"
    context_object_name = "branch_list"


class BranchCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = BranchForm()

        context = {"form": form}

        return render(request, "branch/create.html", context)

    def post(self, request):
        form = BranchForm()

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            contact = form.cleaned_data["contact"]
            address = form.cleaned_data["address"]
            status = form.cleaned_data["status"]

            Branch.objects.create(
                name=name,
                email=email,
                contact=int(contact),
                address=address,
                status=status,
            )
            messages.success(request, "Berhasil membuat branch")
            return redirect("branch")
        else:
            messages.error(request, "gagal membuat branch")
            return redirect()


class BranchUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        branch = Branch.objects.get(id=id)
        form = BranchForm(instance=branch)

        context = {"form": form, "branch": branch}

        return render(request, "branch/update.html", context)

    def post(self, request, id):
        branch = Branch.objects.get(id=id)
        form = BranchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            contact = form.cleaned_data["contact"]
            address = form.cleaned_data["address"]
            status = form.cleaned_data["status"]

            branch.name = name
            branch.email = email
            branch.contact = contact
            branch.address = address
            Branch.status = status

            branch.save()
            messages.success(request, "Berhasil update branch")

            return redirect("branch")
        else:
            messages.error(request, "gagal update branch")
            return redirect("branch")


@login_required(login_url="/auth/login")
def BranchDelete(request, id):
    branch = Branch.objects.get(id=id)

    try:
        branch.delete()
        messages.success(request, "Berhasil delete branch")
        return redirect("branch")
    except Branch.DoesNotExist():
        messages.error(request, "gagal delete branch")

        return redirect("branch")
