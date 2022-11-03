from .models import *
from django import forms


class ResidentialApartmentForm(forms.ModelForm):
    class Meta:
        model = ResidentialApartment
        fields = [
            'name', 'type', 'vacancy', 'power', 'water', 'state', 'city', 'location', 'Address', 'price',
            'negotiable',
            'description', 'power', 'font_image', 'side_image', 'Room1_image', 'Room2_image', 'kitchen_image',
            'Rest_room', 'other_image', 'other_image2',

        ]

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(ResidentialApartmentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(ResidentialApartmentForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = ApartmentType
        fields = [
            'type',
        ]


class CommercialApartmentForm(forms.ModelForm):
    class Meta:
        model = CommercialApartment
        fields = [
            'name', 'type', 'vacancy', 'power', 'state', 'city', 'location', 'Address', 'price', 'negotiable',
            'description', 'power', 'font_image', 'side_image', 'other_image', 'other_image2',

        ]

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(CommercialApartmentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(CommercialApartmentForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst
