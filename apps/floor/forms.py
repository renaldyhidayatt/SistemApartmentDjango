from django import forms
from .models import Floor

class FloorForm(forms.ModelForm):
    floor = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))


    class Meta:
        model = Floor
        fields = ["floor_no"]