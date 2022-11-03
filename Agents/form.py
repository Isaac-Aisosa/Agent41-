from django import forms
from django.forms import ModelForm

from Apartments.models import ResidentialApartment, CommercialApartment
from User_Profiles.models import UserProfiles
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class agent_SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class AgentProfilesForm(forms.ModelForm):
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
        super(AgentProfilesForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(AgentProfilesForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class AgentEditForm(ModelForm):
    class Meta:
        model = UserProfiles
        fields = [
            'full_name',
            'phone',
            'whatsapp',
            'Address',
            'image',

        ]


class AgentResidentialApartmentForm(forms.ModelForm):
    class Meta:
        model = ResidentialApartment
        fields = [
            'landlord_name', 'landlord_phone', 'landlord', 'care_taker', 'name', 'type', 'vacancy', 'power', 'water',
            'state', 'city', 'location', 'Address', 'price',
            'negotiable',
            'description', 'power', 'font_image', 'side_image', 'Room1_image', 'Room2_image', 'kitchen_image',
            'Rest_room', 'other_image', 'other_image2',

        ]

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(AgentResidentialApartmentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(AgentResidentialApartmentForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class AgentCommercialApartmentForm(forms.ModelForm):
    class Meta:
        model = CommercialApartment
        fields = [
            'landlord_name', 'landlord_phone', 'name', 'landlord', 'care_taker', 'type', 'vacancy', 'power', 'state',
            'city', 'location', 'Address', 'price', 'negotiable',
            'description', 'power', 'font_image', 'side_image', 'other_image', 'other_image2',

        ]

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(AgentCommercialApartmentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(AgentCommercialApartmentForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentDetail
        fields = [
            'account_number',
            'account_name',
            'bank',

        ]


class PaymentEditForm(ModelForm):
    class Meta:
        model = PaymentDetail
        fields = [
            'account_number',
            'account_name',
            'bank',

        ]
