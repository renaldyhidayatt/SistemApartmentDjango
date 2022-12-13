from django import forms
from .models import Management

class ManagementForm(forms.ModelForm):
    contact = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    nid = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    member_type = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    joining_date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}))
    status = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))


    class Meta:
        model = Management
        fields = [
            "contact",
            "address",
            "nid",
            "member_type",
            "joining_date",
            "end_date",
            "status"
        ]