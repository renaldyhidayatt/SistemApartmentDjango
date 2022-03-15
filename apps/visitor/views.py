from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from .models import Visitor
from .forms import VisitorForm
from apps.floor.models import Floor
from apps.unit.models import Unit
from apps.month.models import Month
from apps.branch.models import Branch

# Create your views here.
class VisitorList(ListView):
    model = Visitor
    context_object_name = "visitor"
    template_name = "visitor/index.html"

class VisitorCreate(View):
    def get(self, request):
        form = VisitorForm()
        floor = Floor.objects.all()
        unit = Unit.objects.all()
        month = Month.objects.all()
        branch = Branch.objects.all()

        context = {
            "form": form,
            "floor": floor,
            "unit": unit,
            "month": month,
            "branch": branch
        }

        return render(request, "visitor/create.html")

    def post(self, request):
        form = VisitorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            mobile_no = form.cleaned_data["mobile_no"]
            address = form.cleaned_data["address"]
            floor = request.POST["floor"]
            unit = request.POST["unit"]
            intime = form.cleaned_data["intime"]
            outtime = form.cleaned_data["outtime"]
            month = request.POST['month']
            branch = request.POST['branch']

            floor_id = Floor.objects.get(floor_no=floor)
            unit_id = Unit.objects.get(unit_no=unit_id)
            month_id = Month.objects.get(name=month)
            branch_id = Branch.objects.get(name=branch)


            Visitor.objects.create(
                name=name,
                mobile_no=mobile_no,
                address=address,
                floor=floor_id,
                unit=unit_id,
                month=month_id,
                intime=intime,
                outtime=outtime,
                branch=branch_id
            )

            return redirect("visitor")


class VisitorUpdate(View):
    def get(self, request, id):
        visitor = Visitor.objects.get(id=id)
        form = VisitorForm(instance=visitor)
        floor = Floor.objects.all()
        unit = Unit.objects.all()
        month = Month.objects.all()
        branch = Branch.objects.all()

        context = {
            "form": form,
            "floor": floor,
            "unit": unit,
            "month": month,
            "branch": branch
        }

        return render(request, "visitor/create.html")

    def post(self, request,id):
        visitor_id = Visitor.objects.get(id=id)
        form = VisitorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            mobile_no = form.cleaned_data["mobile_no"]
            address = form.cleaned_data["address"]
            floor = request.POST["floor"]
            unit = request.POST["unit"]
            intime = form.cleaned_data["intime"]
            outtime = form.cleaned_data["outtime"]
            month = request.POST['month']
            branch = request.POST['branch']

            floor_id = Floor.objects.get(floor_no=floor)
            unit_id = Unit.objects.get(unit_no=unit_id)
            month_id = Month.objects.get(name=month)
            branch_id = Branch.objects.get(name=branch)

            visitor_id.name=name
            visitor_id.mobile_no = mobile_no
            visitor_id.address = address
            visitor_id.floor = floor_id
            visitor_id.unit = unit_id
            visitor_id.intime = intime
            visitor_id.outtime = outtime
            visitor_id.branch = branch_id

            visitor_id.save()

            return redirect("visitor")




def VisitorDelete(request, id):
    visitor = Visitor.objects.get(id=id)
    try:
        visitor.delete()
        return redirect("visitor")
    except Visitor.DoesNotExist:
        raise Exception("Visitor")