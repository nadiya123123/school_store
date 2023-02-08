from django import forms
from .models import FormData, Department, Course, Purpose, Material


class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address', 'department', 'course', 'purpose',
                  'materials']

        widgets = {
            'dob': forms.TextInput(attrs={'type': 'date'}),
            'materials': forms.CheckboxSelectMultiple(),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['course'].queryset = Course.objects.none()

            if 'department' in self.data:
                try:
                    department_id = int(self.data.get('department'))
                    self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['course'].queryset = self.instance.department.course_set.order_by('name')

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
