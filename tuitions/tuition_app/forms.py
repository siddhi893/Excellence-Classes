from django import forms
from .models import StudentRegistration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = '__all__'
        widgets = {
            'standard': forms.Select(attrs={'id': 'standard'}),
            'board': forms.Select(attrs={'id': 'board'}),
            'subject': forms.Select(attrs={'id': 'subject'}),
            'school': forms.Select(attrs={'id': 'school'}),
            'branch': forms.Select(attrs={'id': 'branch'}),
            'fees': forms.TextInput(attrs={'id': 'fees', 'readonly': True}),
            'payment_mode': forms.Select(attrs={'id': 'payment_mode'}),
            'payment_proof': forms.FileInput(attrs={'id': 'payment_proof'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial empty choices for dependent fields
        self.fields['board'].choices = [('', '-- Select Board --')] + list(self.fields['board'].choices)[1:]
        self.fields['subject'].choices = [('', '-- Select Subject --')] + list(self.fields['subject'].choices)[1:]
        self.fields['school'].choices = [('', '-- Select School --')] + list(self.fields['school'].choices)[1:]