from django import forms
from .models import Departments


class addDepartmentToForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = ['name','phone','describtion']
        