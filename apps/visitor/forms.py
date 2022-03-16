from django import forms
from .models import Visitor

class VisitorForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    intime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}))
    outtime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}))

    class Meta:
        model = Visitor
        fields = [
            "name",
            "mobile_no",
            "address",
            "intime",
            "outtime"
        ]