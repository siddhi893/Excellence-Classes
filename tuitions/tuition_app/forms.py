# tuition_app/forms.py
from django import forms
from .models import StudentRegistration

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4}),
            'fees': forms.TextInput(attrs={'readonly': 'readonly'}),
        }