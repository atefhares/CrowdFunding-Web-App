from django.db import models


# Create your models here.
#
class Country(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    profile_pic = models.ImageField()
    is_activated = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    facebook_profile_id = models.CharField(null=True, blank=True, max_length=45)

    def __str__(self):
        return self.first_name + " " + self.last_name
