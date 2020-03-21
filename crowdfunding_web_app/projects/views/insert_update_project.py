from django.conf import settings
# from datetime import datetime
from django.shortcuts import render

from projects.models import Project


def handle_update_project_request(request):
    return None


def handle_create_new_project_request(request):
    return render(request, "projects/create_project.html")
