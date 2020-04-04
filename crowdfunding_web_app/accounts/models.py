import os

from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
from datetime import timedelta
import datetime

from crowdfunding_web_app.settings import MEDIA_URL


class Country(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


def one_day_hence():
    return timezone.now() + timezone.timedelta(hours=24)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="user_profile")
    phone_number = models.CharField(max_length=45, default=None, null=True)
    profile_pic = models.ImageField(default=os.path.join('profile_pic', 'jo.jpg')
                                    , upload_to='profile_pic')
    birth_date = models.DateField(null=True, default=None)
    country = CountryField(null=True, blank=True)
    facebook_profile_id = models.CharField(
        null=True, blank=True, max_length=45)
    time_stamp = models.DateTimeField(default=timezone.now)
    expires = models.DateTimeField(default=one_day_hence)
    is_active = models.BooleanField(default=False)
    key = models.CharField(null=False, blank=False,
                           max_length=45, default=None)
    once_activation = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.email} UserProfile'
