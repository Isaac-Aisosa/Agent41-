from django import forms
from django.forms import ModelForm

from Agents.models import PaymentDetail
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LL_SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LandlordProfilesForm(forms.ModelForm):
    class Meta:
        model = UserProfiles
        fields = [
            'full_name',
            'phone',
            'whatsapp',
            'Address',
            'image',

        ]

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(LandlordProfilesForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(LandlordProfilesForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class LandlordProfilesEditForm(ModelForm):
    class Meta:
        model = UserProfiles
        fields = [
            'full_name',
            'phone',
            'whatsapp',
            'Address',
            'image',
        ]
