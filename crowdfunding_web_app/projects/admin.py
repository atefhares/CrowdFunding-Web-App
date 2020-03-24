from django.contrib import admin
from projects.models import *

# Register your models here.

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ProjectPicture)
admin.site.register(Donation)
admin.site.register(ProjectRating)
admin.site.register(Comment)
admin.site.register(CommentReply)
admin.site.register(ProjectReport)
admin.site.register(CommentReport)


