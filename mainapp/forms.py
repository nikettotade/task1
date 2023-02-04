from django import forms
from .models import School, Student

# creating forms for school

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'create_at', 'update_at']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'create_at': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'update_at': forms.DateTimeInput(attrs={'class': 'form-control'})
        }

    # this function will be used for the validation
    def clean(self):
        super(SchoolForm, self).clean()
        name = self.cleaned_data.get('name')
        if len(name) < 4:
            raise forms.ValidationError('Name must be 4 character')

        return self.cleaned_data


# creating forms for student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'enrollment', 'school', 'create_at', 'update_at']
        school = forms.ModelChoiceField(
            queryset=School.objects.all(),
            empty_label=None,
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'enrollment': forms.TextInput(attrs={'class': 'form-control'}),
            'school': forms.Select(attrs={'class': 'form-control'}),
            'create_at': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'update_at': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

    # this function will be used for the validation
    def clean(self):
        super(StudentForm, self).clean()
        name = self.cleaned_data.get('name')
        if len(name) < 4:
            raise forms.ValidationError('Name must be 4 character')

        return self.cleaned_data