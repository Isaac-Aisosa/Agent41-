# Generated by Django 3.2.7 on 2021-10-25 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='full name', max_length=100, verbose_name='Full Name')),
                ('phone', models.CharField(max_length=15, verbose_name='Mobile number')),
                ('whatsapp', models.CharField(max_length=15, verbose_name='Whatsapp number')),
                ('Address', models.CharField(max_length=255, verbose_name='Home address')),
                ('image', models.ImageField(default='profile_image.png', null=True, upload_to='media/landlord/profileImage', verbose_name='Profile Image')),
                ('landlord', models.BooleanField(default=False)),
                ('agent', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('reg_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Reg.date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Reg_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]