import os

from django.conf.global_settings import MEDIA_URL
from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField

from accounts.models import User
import datetime
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Tag(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="projects")
    title = models.CharField(max_length=45)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_target = models.DecimalField(max_digits=20, decimal_places=10)
    start_date = models.DateField()
    end_date = models.DateField()
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="List of tags", related_name="number_of_uses")
    country = CountryField(null=False, blank=False)

    @property
    def pledged_amount(self):
        return self.donations.aggregate(Sum('amount'))

    def __str__(self):
        return self.title


def get_upload_path_project_picture(instance, filename):
    return os.path.join(MEDIA_URL, 'project_pictures', instance.project.title, filename)


class ProjectPicture(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="pictures")
    pic_path = models.FileField(db_column="pic_path",
                                upload_to=get_upload_path_project_picture)

    def __str__(self):
        return f"{self.project.title} | {str(self.pic_path)}"


class Donation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="donations")
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return f"{self.user} of ${self.amount} to {self.project}"


class ProjectRating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_rating")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rated_project")
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.project.title}  |  {self.rating}"


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="comments")
    created_at = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=600)
    comment_reports = models.SmallIntegerField(default=0)
    is_reported = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user} on {self.project}"


class CommentReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.TextField()

    def __str__(self):
        return f"{self.user} on {self.comment}"


class ProjectReport(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    report_description = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.user} on {self.project}"


class CommentReport(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    report_description = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.user} on {self.comment}"
