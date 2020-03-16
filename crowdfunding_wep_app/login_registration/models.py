from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=45)


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    profile_pic = models.CharField(max_length=45)
    is_activated = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    facebook_profile_id = models.CharField(max_length=45)
