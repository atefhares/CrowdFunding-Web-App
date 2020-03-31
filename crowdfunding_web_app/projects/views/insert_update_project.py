from django.conf import settings
# from datetime import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from projects.models import Project


def handle_update_project_request(request):
    return None


def handle_create_new_project_request(request):
    print(request)
    print(request.POST)
    print(request.POST.get("category"))
    return render(request, "projects/create_project.html")
