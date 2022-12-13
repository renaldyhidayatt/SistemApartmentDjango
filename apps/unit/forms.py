from django import forms
from .models import Unit

class UnitForm(forms.ModelForm):
    unit_no = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))



    class Meta:
        model = Unit
        fields = [
            "unit_no"
        ]