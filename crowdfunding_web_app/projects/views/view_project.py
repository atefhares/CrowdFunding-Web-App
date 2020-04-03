from django.conf import settings
from django.shortcuts import render, redirect

from projects.models import Project


def handle_view_project_request(request, project_id):
    if settings.DEBUG:
        print("request: ", request)
        print("project_id: ", project_id)

    context = {'project': get_project(project_id)}
    print(context)
    return render(request, "projects/project_details.html", context)


def get_project(id):
    project = Project.objects.get(id=id)
    return project
