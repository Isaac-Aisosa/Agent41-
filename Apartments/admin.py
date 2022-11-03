from django.contrib import admin
from .models import *

admin.site.register(ApartmentType)
admin.site.register(ApartmentTypeCommercial)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Location)
admin.site.register(ResidentialApartment)
admin.site.register(CommercialApartment)
admin.site.register(ResidentialApartmentRequest)
admin.site.register(CommercialApartmentRequest)
