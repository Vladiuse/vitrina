from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'phone', 'offer', 'ip']
        widgets = {
            'offer': forms.HiddenInput(),
            'ip': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': "form__contact-input"}),
            'phone': forms.TextInput(attrs={'class': "form__contact-input"}),
        }
        labels  = {
            'name': 'Nombre',
            'phone': 'Teléfono',
        }