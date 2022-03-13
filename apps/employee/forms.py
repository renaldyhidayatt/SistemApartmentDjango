from django import forms
from .models import Employee, EmployeeSalary

class EmployeeForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    nid = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    designation = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}))
    ending_date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}))
    

    class Meta:
        model = Employee
        fields = [
            "address",
            "nid",
            "designation",
            "date",
            "ending_date"
        ]


class EmployeeSalaryForm(forms.ModelForm):
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    
    

