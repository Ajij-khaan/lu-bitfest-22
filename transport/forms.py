import code
from django.contrib.auth.models import User
from django import forms
from .models import BusInfo
from django.utils.translation import gettext_lazy as _


class BusSignForm(forms.ModelForm):
    class Meta:
        model = BusInfo
        fields = ['license_number', 'codename',
                  'capacity', 'drive_name', 'driver_contact', 'is_active']
        labels = {'drive_name': 'Driver Name'}

        widgets = {
            'license_number': forms.TextInput(attrs={'placeholder': 'Licence Number', 'class': 'form-control'}),
            'codename': forms.TextInput(attrs={'placeholder': 'Code Name', 'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'placeholder': 'Capacity', 'class': 'form-control'}),
            'drive_name': forms.TextInput(attrs={'placeholder': 'Name....', 'class': 'form-control'}),
            'driver_contact': forms.NumberInput(attrs={'placeholder': 'Contact', 'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }

    def clean_codename(self):
        codename = self.cleaned_data['codename']
        if BusInfo.objects.filter(codename=codename).exists():
            raise forms.ValidationError("Codename Already Exists")

        return codename
