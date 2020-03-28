from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=45,default=None,null=True)
    profile_pic = models.ImageField(null=True)
    birth_date = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    facebook_profile_id = models.CharField(null=True, blank=True, max_length=45)
    def __str__(self):
        return self.user.email

