from django.db import models
from django_countries.fields import CountryField

from django.contrib.auth.models import User
# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=45, default=None, null=True)
    profile_pic = models.ImageField(null=True)
    birth_date = models.DateField(null=True, blank=True)
    country = CountryField(null=True)
    facebook_profile_id = models.CharField(
        null=True, blank=True, max_length=45)
    time_stamp = models.DateTimeField(null=True)
    expires = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=False)
    key = models.CharField(null=False, blank=False,
                           max_length=45, default=None)
    once_activation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
