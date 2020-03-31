from django.contrib import admin

# Register your models here.
from admins.models import FeaturedProject, Admin

admin.site.register(Admin)
admin.site.register(FeaturedProject)
