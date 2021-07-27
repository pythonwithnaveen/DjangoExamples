from django import forms
from app1.models import  EmployeeModel,AccountModel


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = "__all__"


class AccountForm(forms.ModelForm):


    class Meta:
        model = AccountModel
        fields = "__all__"