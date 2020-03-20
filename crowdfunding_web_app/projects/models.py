from django.db import models
from login_registration.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=45)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_target = models.DecimalField(max_digits=20, decimal_places=10)
    start_date = models.DateField()
    end_date = models.DateField()
    tags = models.ManyToManyField(Tags, blank=True,
                                  verbose_name="List of tags",
                                  related_name="number_of_uses")

    def __str__(self):
        return self.title


class ProjectPicture(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    pic_path = models.CharField(max_length=45)

    def __str__(self):
        return self.project


class Donation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return f"{self.user} of ${self.amount} to {self.project}"


class ProjectRating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.user} on {self.project}"


class CommentReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.TextField()

    def __str__(self):
        return f"{self.user} on {self.comment}"


class ProjectReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    report_description = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.user} on {self.project}"


class CommentReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    report_description = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.user} on {self.comment}"
