from django import forms
from .models import Utility

class UtilityForm(forms.ModelForm):
    gas_bill = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    security_bill = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Utility
        fields = [
            "gas_bill",
            "security_bill"
        ]