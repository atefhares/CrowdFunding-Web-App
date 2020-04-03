from django.conf import settings
from django.shortcuts import render, redirect


def handle_view_project_request(request, project_id):
    if settings.DEBUG:
        print("request: ", request)
        print("project_id: ", project_id)

    context = {}

    return render(request, "projects/project_details.html", context)
