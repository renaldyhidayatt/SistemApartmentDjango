from django import forms
from .models import Month

class MonthForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Month
        fields = [
            "name"
        ]