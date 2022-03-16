from django import forms
from .models import Year

class YearForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Year
        fields = [
            "name"
        ]