from django.db import models
from login_registration.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=45)


class Tags(models.Model):
    name = models.CharField(max_length=45)


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=45)
    description = models.TextField
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_target = models.DecimalField
    start_date = models.DateField
    end_date = models.DateField
    tags = models.ManyToManyField(Tags, blank=True, verbose_name="List of tags", related_name="number_of_uses")
