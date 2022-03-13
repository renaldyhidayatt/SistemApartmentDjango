from django import forms
from .models import Complain


class ComplainForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}))
    

    class Meta:
        model = Complain
        fields = [
            "title",
            "desciption",
            "date"
        ]
