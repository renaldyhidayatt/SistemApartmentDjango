from django import forms
from .models import Branch

class BranchForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Branch"}))
    contact = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Contact"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Address"}))
    status = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Status"}))


    class Meta:
        model = Branch
        fields = [
            "name",
            "email",
            "contact",
            "address",
            "status"
        ]