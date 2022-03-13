from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from .models import BuildingInfo
from .forms import BuildingForm
from apps.branch.models import Branch

# Create your views here.
class BuildingList(ListView):
    model = BuildingInfo
    template_name = "building/index.html"
    context_object_name = "building_list"


class BuildingCreate(View):
    def get(self, request):
        form = BuildingForm

        context = {
            "form": form
        }

        return render(request, "building/create.html", context)

    def post(self, request):
        form = BuildingForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data["name"]
            address = form.cleaned_data["address"]
            securityGuardMobile = form.cleaned_data["securityGuardMobile"]
            secratatyMobile = form.cleaned_data["secratatyMobile"]
            moderatorMobile = form.cleaned_data["moderatorMobile"]
            buildingMakeYear = form.cleaned_data["buildingMakeYear"]
            b_name = form.cleaned_data["b_name"]
            b_address = form.cleaned_data["b_address"]
            b_phone = form.cleaned_data["b_phone"]
            buildingImage = form.cleaned_data["buildingImage"]
            branch = request.POST["branch"]

            do = Branch.objects.get(name=branch)


            BuildingInfo.objects.create(
                name=name,
                address=address,
                securityGuardMobile=securityGuardMobile,
                secratatyMobile=secratatyMobile,
                moderatorMobile=moderatorMobile,
                buildingMakeYear=buildingMakeYear,
                b_name=b_name,
                b_address=b_address,
                b_phone=b_phone,
                buildingImage=buildingImage,
                branch=do
            )

            return redirect("building")


class BuildingUpdate(View):
    def get(self, request, id):
        building = BuildingInfo.objects.get(id=id)
        form = BuildingForm(instance=building)

        context = {
            "form": form
        }

        return render(request, "building/update.html", context)

    def post(self, request, id):
        building = BuildingInfo.objects.get(id=id)
        form = BuildingForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            address = form.cleaned_data["address"]
            securityGuardMobile = form.cleaned_data["securityGuardMobile"]
            secratatyMobile = form.cleaned_data["secratatyMobile"]
            moderatorMobile = form.cleaned_data["moderatorMobile"]
            buildingMakeYear = form.cleaned_data["buildingMakeYear"]
            b_name = form.cleaned_data["b_name"]
            b_address = form.cleaned_data["b_address"]
            b_phone = form.cleaned_data["b_phone"]
            buildingImage = form.cleaned_data["buildingImage"]
            branch = request.POST["branch"]

            do = Branch.objects.get(name=branch)

            building.name = name
            building.address = address
            building.securityGuardMobile =  securityGuardMobile
            building.secratatyMobile = secratatyMobile
            building.moderatorMobile = moderatorMobile
            building.buildingMakeYear = buildingMakeYear
            building.b_name = b_name
            building.b_address = b_address
            building.b_phone = b_phone
            building.buildingImage = buildingImage
            building.branch = do

            building.save()

            return redirect("building")

        
def BuildingDelete(request, id):
    building = BuildingInfo.objects.get(id=id)

    try:
        building.delete()
        return redirect("building")
    except BuildingInfo.DoesNotExist:
        raise Exception("Baisia")
