from django import forms
from .models import BuildingInfo

class BuildingForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Address"}))
    securityGuardMobile = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Security Guard Mobile"}))
    secratatyMobile = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "secratatyMobile"}))
    moderatorMobile = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "moderatorMobile"}))
    buildingMakeYear = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "buildingMakeYear"}))
    b_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "building name"}))
    b_address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "building address"}))
    b_phone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "building phone"}))
    buildingImage = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}))


    class Meta:
        model = BuildingInfo
        fields = [
            "name",
            "address",
            "securityGuardMobile",
            "secratatyMobile",
            "moderatorMobile",
            "buildingMakeYear",
            "b_name",
            "b_address",
            "b_phone",
            "buildingImage"
        ]
