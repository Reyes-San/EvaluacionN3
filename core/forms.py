from django import forms
from .models import Employee, Department, Area


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['name', 'lastname', 'occupation', 'department', 'avatar']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last_Name'}),
            'occupation': forms.Textarea(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'select form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['name', 'description', 'area']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', }),
            'area': forms.Select(attrs={'class': 'select form-control'})
        }


class AreaForm(forms.ModelForm):

    class Meta:
        model = Area
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre_Area'})
        }
