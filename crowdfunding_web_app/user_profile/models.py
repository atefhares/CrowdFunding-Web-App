from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from accounts.models import UserProfile
admin.site.register(UserProfile)