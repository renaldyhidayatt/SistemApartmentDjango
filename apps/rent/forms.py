from django import forms
from .models import Rent

class RentForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    nid = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    advance = forms.DecimalField(widget=forms.TextInput(attrs={"class": "form-control"}))
    rent_pm = forms.DecimalField(widget=forms.TextInput(attrs={"class": "form-control"}))
    date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}))

    class Meta:
        model = Rent
        fields = [
            "address",
            "nid",
            "advance",
            "rent_pm",
            "date"

        ]