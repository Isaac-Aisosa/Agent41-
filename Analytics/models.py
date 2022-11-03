from django.db import models
from Apartments.models import ResidentialApartment, CommercialApartment
# Create your models here.


class Visit(models.Model):
    request = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.timestamp}'


class VisitedResidentialApartment(models.Model):
    apartment = models.ForeignKey(ResidentialApartment, related_name="Res_apartment", on_delete=models.CASCADE)
    request = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.timestamp}'


class VisitedCommercialApartment(models.Model):
    apartment = models.ForeignKey(CommercialApartment, related_name="comm_apartment", on_delete=models.CASCADE)
    request = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.timestamp}'