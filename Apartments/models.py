from django.db import models
from PIL import Image
from django.conf import settings
from django.db import models


# Create your models here.


class ApartmentType(models.Model):
    type = models.CharField(verbose_name='Type of Apartment', max_length=225, null=False, blank=False, )

    def __str__(self):
        return f'{self.type}'


class ApartmentTypeCommercial(models.Model):
    type = models.CharField(verbose_name='Type of Apartment', max_length=225, null=True, blank=True, )

    def __str__(self):
        return f'{self.type}'


class State(models.Model):
    state = models.CharField(verbose_name='State', max_length=225, null=True, blank=True, )

    def __str__(self):
        return f'{self.state}'


class City(models.Model):
    city = models.CharField(verbose_name='city', max_length=225, null=True, blank=True, )

    def __str__(self):
        return f'{self.city}'


class Location(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location = models.CharField(verbose_name='location', max_length=225, null=True, blank=True, )

    def __str__(self):
        return f'{self.city}, {self.location}'


POWER = (
    ("24 hours daily", "24hours daily"),
    ("20 hours daily", "20 hours daily"),
    ("18 hours daily", "18 hours daily"),
    ("10 hours daily", "10 hours daily"),
    ("8 hours daily", "8 hours daily"),
    ("6 hours daily", "6 hours daily"),
    ("4 hours daily", "4 hours daily"),
    ("3 hours daily", "3 hours daily"),
    ("2 hours daily", "2 hours daily"),
    ("1 hour daily", "1 hour daily"),
    ("No power", "No power"),
)

WATER = (
    ("Borehole water Available inside apartment", "Borehole water Available inside apartment"),
    ("Borehole water Available outside apartment", "Borehole water Available outside apartment"),
    ("Borehole water Available close to apartment", "Borehole water Available close to apartment"),
    ("Borehole water far from apartment", "Borehole water far from apartment"),
    ("Reservoir is Available", "Reservoir is Available"),
    ("Borehole water and Reservoir is Available", "Borehole water and Reservoir is Available"),
    ("No water", "No water"),
)


class ResidentialApartment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="registered_by", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Apartment Name', max_length=100, null=False, blank=False, )
    landlord = models.BooleanField(default=True)
    care_taker = models.BooleanField(default=False)
    landlord_name = models.CharField(verbose_name='Landlord or CareTaker Name', max_length=100, null=True, blank=True,
                                     )
    landlord_phone = models.CharField(verbose_name='Landlord or CareTaker phone', max_length=100, null=True,
                                      blank=True, )
    description = models.TextField(verbose_name='Description', max_length=225, null=True, blank=True, )
    type = models.ForeignKey(ApartmentType, on_delete=models.CASCADE)
    power = models.CharField(verbose_name='Power Status', max_length=150, choices=POWER, default="Power Status")
    water = models.CharField(verbose_name='Water Status', max_length=150, choices=WATER, default="Water Status")
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    Address = models.CharField(verbose_name='Full Address', max_length=1000, null=True, blank=True, )
    price = models.BigIntegerField(default=0, verbose_name='Yearly Price', null=False, blank=False, )
    negotiable = models.BooleanField(default=False, verbose_name='Negotiable', )
    vacant = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="approved_by_user", on_delete=models.CASCADE, null=True, blank=True,)
    unapproved = models.BooleanField(default=False)
    star = models.IntegerField(default=1, null=True, blank=True)
    residential = models.BooleanField(default=True)
    vacancy = models.BigIntegerField(default=0, null=True, blank=True, )
    font_image = models.FileField(verbose_name='FontView Image',
                                  upload_to=f' media/Apartment/Residential/', default='noImage.png',
                                  null=False,
                                  blank=False, )
    side_image = models.FileField(verbose_name='SideView Image',
                                  upload_to=f' media/Apartment/Residential/', default='noImage.png', null=False,
                                  blank=False, )
    Room1_image = models.FileField(verbose_name='Room Image',
                                   upload_to=f' media/Apartment/Residential/', default='noImage.png', null=True,
                                   blank=True, )
    Room2_image = models.FileField(verbose_name='Setting Room Image',
                                   upload_to=f' media/Apartment/Residential/', default='noImage.png', null=True,
                                   blank=True, )
    kitchen_image = models.FileField(verbose_name='kitchen Image',
                                     upload_to=f' media/Apartment/Residential/', default='noImage.png', null=True,
                                     blank=True, )
    Rest_room = models.FileField(verbose_name='Rest Room Image',
                                 upload_to=f' media/Apartment/Residential/', default='noImage.png', null=True,
                                 blank=True, )
    other_image = models.FileField(verbose_name='other Image',
                                   upload_to=f' media/Apartment/Residential/', default='noImage.png', null=True,
                                   blank=True, )
    other_image2 = models.FileField(verbose_name='other Image',
                                    upload_to=f' media/Apartment/Residential/', default='noImage.png', null=True,
                                    blank=True, )

    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.user},{self.name} '


class CommercialApartment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="commercial_apartment_landlord", on_delete=models.CASCADE, )
    name = models.CharField(verbose_name='Apartment Name', max_length=100, null=False, blank=False, )
    landlord = models.BooleanField(default=True)
    care_taker = models.BooleanField(default=False)
    landlord_name = models.CharField(verbose_name='Landlord or CareTaker Name', max_length=100, null=True, blank=True,
                                     )
    landlord_phone = models.CharField(verbose_name='Landlord or CareTaker phone', max_length=100, null=True,
                                      blank=True, )
    description = models.TextField(verbose_name='Description', max_length=225, null=True, blank=True, )
    type = models.ForeignKey(ApartmentTypeCommercial, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    power = models.CharField(verbose_name='Power Status', max_length=150, choices=POWER, default="Power Status")
    Address = models.CharField(verbose_name='Full Address', max_length=1000, null=True, blank=True, )
    price = models.BigIntegerField(default=0, verbose_name='Yearly Price', null=False, blank=False, )
    negotiable = models.BooleanField(default=False, verbose_name='Is Price Negotiable', )
    vacant = models.BooleanField(default=True)
    vacancy = models.BigIntegerField(default=0, null=True, blank=True, )
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="comm_approved_by_user", on_delete=models.CASCADE,null=True, blank=True,)
    unapproved = models.BooleanField(default=False)
    star = models.IntegerField(default=1, null=True, blank=True)
    commercial = models.BooleanField(default=True)

    font_image = models.FileField(verbose_name='FontView Image', default='noImage.png',
                                  upload_to=f' media/Apartment/commercial/', null=False,
                                  blank=False, )
    side_image = models.FileField(verbose_name='SideView Image', default='noImage.png',
                                  upload_to=f' media/Apartment/commercial/', null=False,
                                  blank=False, )
    other_image = models.FileField(verbose_name='other Image', default='noImage.png',
                                   upload_to=f' media/Apartment/commercial/', null=True,
                                   blank=True, )
    other_image2 = models.FileField(verbose_name='other Image', default='noImage.png',
                                    upload_to=f' media/Apartment/commercial/', null=True,
                                    blank=True, )

    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f' {self.user},{self.name} '


class ResidentialApartmentRequest(models.Model):
    apartment = models.ForeignKey(ResidentialApartment, related_name="Residential_apartment", on_delete=models.CASCADE)
    client = models.CharField(verbose_name='Client Name', max_length=225, null=False, blank=False, )
    phone = models.CharField(max_length=15, verbose_name='phone number', null=False, blank=False, )
    seen = models.BooleanField(default=False)
    comfirmed = models.BooleanField(default=False)
    service_fee = models.BooleanField(default=False)
    agent_fee = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="confirm_by", on_delete=models.CASCADE, null=True, blank=True, )
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.client} Requested for {self.apartment}'


class CommercialApartmentRequest(models.Model):
    apartment = models.ForeignKey(CommercialApartment, related_name="Commercial_apartment", on_delete=models.CASCADE)
    client = models.CharField(verbose_name='Client Name', max_length=225, null=False, blank=False, )
    phone = models.CharField(max_length=15, verbose_name='phone number', null=False, blank=False, )
    seen = models.BooleanField(default=False)
    comfirmed = models.BooleanField(default=False)
    service_fee = models.BooleanField(default=False)
    agent_fee = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="confirm_by_comm", on_delete=models.CASCADE, null=True, blank=True, )
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.client} Requested for {self.apartment}'
