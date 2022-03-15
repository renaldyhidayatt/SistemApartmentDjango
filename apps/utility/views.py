from django.shortcuts import render
from django.views.generic import ListView, View
from .forms import UtilityForm
from .models import Utility


# Create your views here.
class UtilityList(ListView):
    model = Utility
    context_object_name = "unit"
    template_name = "utility/index.html"

class UtilityCreate(View):
    def get(self, request):
        form = UtilityForm()
        context = {
            "form": form
        }
        return render(request, "utility/create.html", context)

    def post(self, request):
        form = UtilityForm(request.POST)
        if form.is_valid():
            gas_bill = form.cleaned_data["gas_bill"]
            security_bill = form.cleaned_data["security_bill"]

            Utility.objects.create(
                gas_bill=gas_bill,
                security_bill=security_bill
            )

            return redirect("utility")


class UtilityUpdate(View):
    def get(self, request, id):
        utility = Utility.objects.get(id=id)
        form = UtilityForm(instance=utility)
        context = {
            "form": form
        }
        return render(request, "utility/create.html", context)


    def post(self, request, id):
        form = UtilityForm(request.POST)
        if form.is_valid():
            gas_bill = form.cleaned_data["gas_bill"]
            security_bill = form.cleaned_data["security_bill"]

            Utility.objects.create(
                gas_bill=gas_bill,
                security_bill=security_bill
            )

            return redirect("utility")


def UtilityDelete(request,id):
    utility = Utility.objects.get(id=id)
    try:
        utility.delete()
        return redirect("utility")
    except Utility.DoesNotExist:
        raise Exception("utility")