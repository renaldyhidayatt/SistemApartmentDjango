from django import forms
from .models import Bill


class BillForm(forms.ModelForm):
    type = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}))
    total_amount = forms.DecimalField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    deposit_bank = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    details = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Bill
        fields = ["type", "date", "total_amount","deposit_bank","details"]
