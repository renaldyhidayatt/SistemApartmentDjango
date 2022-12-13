from django import forms
from .models import Fund

class FundForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}))
    total_amount = forms.DecimalField(widget=forms.TextInput(attrs={"class":"form-control"}))
    purpose = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Fund
        fields = [
            "date",
            "total_amount",
            "purpose"
        ]
