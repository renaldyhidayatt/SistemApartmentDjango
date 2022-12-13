from django import forms
from .models import Fair


class FairForm(forms.ModelForm):
    type = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    rid = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    water_bill = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    electric_bill = forms.DecimalField(widget=forms.TextInput(attrs={"class": "form-control"}))
    gas_bill = forms.DecimalField(widget=forms.TextInput(attrs={"class": "form-control"}))
    security_bill = forms.DecimalField(widget=forms.TextInput(attrs={"class": "form-control"}))
    utility_bill = forms.DecimalField(widget=forms.TextInput(attrs={"class": "form-control"}))
    other_bill = forms.DecimalField(widget=forms.TextInput(attrs={"class": "form-control"}))
    total_rent = forms.DecimalField(widget=forms.TextInput(attrs={"class": "form-control"}))
    issue_date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}))


    class Meta:
        model = Fair
        fields = [
            "type",
            "rid",
            "water_bill",
            "electric_bill",
            "gas_bill",
            "security_bill",
            "utility_bill",
            "other_bill",
            "total_rent",
            "issue_date"
        ]