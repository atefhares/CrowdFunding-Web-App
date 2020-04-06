from django.db import models

# Create your models here.
from accounts.models import User
from projects.models import Project


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class FeaturedProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="featured_project")
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    date_featured = models.DateField()

    def __str__(self):
        return self.project.title
