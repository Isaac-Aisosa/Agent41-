from PIL import Image
from django.conf import settings
from django.db import models


# Create your models here.

class UserProfiles(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='Reg_by', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, verbose_name="Full Name", default='full name', null=False, blank=False)
    phone = models.CharField(max_length=15, verbose_name="Mobile number", null=False, blank=False)
    whatsapp = models.CharField(max_length=15, verbose_name="Whatsapp number", null=False, blank=False)
    Address = models.CharField(verbose_name='Home address', max_length=255)
    image = models.ImageField(verbose_name='Profile Image', default='profile_image.png',
                              upload_to='media/landlord/profileImage', null=True, )
    landlord = models.BooleanField(default=False)
    agent = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    apartment = models.BigIntegerField(default=0, null=True, blank=True)

    reg_date = models.DateTimeField(verbose_name='Reg.date', auto_now_add=True,
                                    editable=False, null=True, blank=True, )

    def __str__(self):
        return f'{self.user}'

    def save(self, *arg, **kwargs):
        super().save(*arg, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
