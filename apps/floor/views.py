from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import Floor
from .forms import FloorForm
from apps.branch.models import Branch

# Create your views here.

class FloorList(ListView):
    model = Floor
    template_name = "floor/index.html"
    context_object_name = "floor_list"


class FloorCreate(View):
    def get(self, request):
        form = FloorForm()
        branch = Branch.objects.all()


        context = {
            "form": form,
            "branch": branch
        }

        return render(request, "floor/create.html", context)

    def post(self, request):
        form = FloorForm(request.POST)
        if form.is_valid():
            floor_no = form.cleaned_data["floor_no"]
            branch = request.POST["branch"]
            
            branch_id = Branch.objects.get(name=branch)

            Floor.objects.create(
                floor_no=floor_no,
                branch=branch_id
            )

            return redirect("floor")
            



class FloorUpdate(View):
    def get(self, request, id):
        floor = Floor.objects.get(id=id)
        form = FloorForm(instance=floor)
        branch = Branch.objects.all()


        context = {
            "form": form,
            "branch": branch,
            "floor": floor
        }

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

            return redirect("floor")






def FloorDelete(request,id):
    floor = Floor.objects.get(id=id)

    try:
        floor.delete()
        return redirect("floor")
    except Floor.DoesNotExist:
        raise Exception("Floor")

