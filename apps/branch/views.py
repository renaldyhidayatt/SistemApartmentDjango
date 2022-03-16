from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from .forms import BranchForm
from .models import Branch



# Create your views here.
class BranchList(ListView):
    model = Branch
    template_name = "branch/index.html"
    context_object_name = "branch_list"

class BranchCreate(View):
    def get(self, request):
        form = BranchForm()

        context = {
            "form": form
        }

        return render(request, "branch/create.html", context)

    def post(self, request):
        form = BranchForm()

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = forms.cleaned_data["email"]
            contact = forms.cleaned_data["contact"]
            address = forms.cleaned_data["address"]
            status = forms.cleaned_data["status"]

            Branch.objects.create(
                name=name,
                email=email,
                contact=int(contact),
                address=address,
                status=status
            )

            return redirect("branch")


class BranchUpdate(View):
    def get(self, request,id):
        branch = Branch.objects.get(id=id)
        form = BranchForm(instance=branch) 

        context = {
            "form": form,
            "branch": branch
        }       

        return render(request, "branch/update.html", context)

    def post(self, request,id):
        branch = Branch.objects.get(id=id)
        form = BranchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = forms.cleaned_data["email"]
            contact = forms.cleaned_data["contact"]
            address = forms.cleaned_data["address"]
            status = forms.cleaned_data["status"]

            branch.name = name
            branch.email = email
            branch.contact = contact
            branch.address = address
            Branch.status = status

            branch.save()

            return redirect("branch")




def BranchDelete(request,id):
    branch = Branch.objects.get(id=id)

    try:
        branch.delete()
    except Branch.DoesNotExist():
        raise Exception("Salah")