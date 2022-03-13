from django import forms
from .models import Maintance

class MaintanceForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}))
    amount = forms.DecimalField(widget=forms.TextInput(attrs={"class": "form-control"}))
    details = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Maintance
        fields = [
            'title',
            "date",
            "amount",
            "details"
        ]