from django.contrib.auth.models import User
from django import forms
from .models import TransportUser, ConsumerUser
from django.utils.translation import gettext_lazy as _


class TransportSignForm(forms.ModelForm):
    class Meta:
        model = TransportUser
        fields = ['username', 'contact_number',
                  'password', 'cpassword']
        labels = {'cpassword': 'Confirm Password'}

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Mobile', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
            'cpassword': forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}),

        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if TransportUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Username Already Exists")

        return username

    def clean_contact_number(self):
        contact_number = self.cleaned_data['contact_number']
        if TransportUser.objects.filter(contact_number=contact_number).exists():
            raise forms.ValidationError("Mobile Number Already Exists")

        return contact_number


class ConsumerUserForm(forms.ModelForm):
    class Meta:
        model = ConsumerUser
        fields = ('role', 'user_name', 'id_no', 'contact_number',
                  'pickup_stopage', 'password', 'cpassword')

        widgets = {
            'role': forms.Select(attrs={'placeholder': 'Role', 'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'placeholder': 'User Name', 'class': 'form-control'}),
            'id_no': forms.NumberInput(attrs={'placeholder': 'Id No', 'class': 'form-control'}),
            'contact_number': forms.NumberInput(attrs={'placeholder': 'Contact Number', 'class': 'form-control'}),
            'pickup_stopage': forms.Select(attrs={'placeholder': 'pickup_stopage',  'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'password',  'class': 'form-control'}),
            'cpassword': forms.PasswordInput(attrs={'placeholder': 'confirm password',  'class': 'form-control'}),
        }

        def clean_username(self):
            username = self.cleaned_data['username']
            if TransportUser.objects.filter(username=username).exists():
                raise forms.ValidationError("Username Already Exists")

            return username

        def clean_contact_number(self):
            contact_number = self.cleaned_data['contact_number']
            if TransportUser.objects.filter(contact_number=contact_number).exists():
                raise forms.ValidationError("Mobile Number Already Exists")

            return contact_number

        def clean_id_no(self):
            id_no = self.cleaned_data['id_no']
            if TransportUser.objects.filter(id_no=id_no).exists():
                raise forms.ValidationError("Id No Already Exists")

            return id_no
