from cProfile import label
import code
import imp
from django.contrib.auth.models import User
from django import forms

from django.utils.translation import gettext_lazy as _

from transport.models import UpdateTransportProfile, UpdateStudentProfile
from consumer.models import RequestBus


class UpdateProfileTeacherForm(forms.ModelForm):
    class Meta:
        model = UpdateTransportProfile
        fields = ['department', 'codename', 'designation']

        widgets = {
            'department': forms.Select(attrs={'placeholder': 'Department', 'class': 'form-control'}),
            'codename': forms.TextInput(attrs={'placeholder': 'Codename', 'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'placeholder': 'Designation', 'class': 'form-control'}),
        }


class UpdateProfileStudentForm(forms.ModelForm):
    class Meta:
        model = UpdateStudentProfile
        fields = ['fullname', 'batch', 'section']

        widgets = {
            'fullname': forms.TextInput(attrs={'placeholder': 'FullName', 'class': 'form-control'}),
            'batch': forms.TextInput(attrs={'placeholder': 'Batch', 'class': 'form-control'}),
            'section': forms.TextInput(attrs={'placeholder': 'Section', 'class': 'form-control'}),
        }


class RequestBusForm(forms.ModelForm):
    class Meta:
        model = RequestBus
        fields = ['root_bus']

        widgets = {
            'root_bus': forms.Select(attrs={'class': 'form-control'}),

        }
