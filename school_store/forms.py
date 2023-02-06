from django import forms
from .models import FormData, Department, Course, Purpose, Material


class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address', 'department', 'course', 'purpose',
                  'materials']

        widgets = {
            'dob': forms.TextInput(attrs={'type': 'date'}),
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['department', 'name']


class PurposeForm(forms.ModelForm):
    class Meta:
        model = Purpose
        fields = ['name']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name']