from django.conf import settings
# from datetime import datetime
from django.shortcuts import render

from projects.models import Project


def handle_list_all_projects_request(request):
    if settings.DEBUG:
        print("request: ", request)

    all_projects = Project.objects.filter()

    # if settings.DEBUG:
        # print("all_projects: ", all_projects)

    projects_data_list = []
    for project in all_projects:
        projects_data_list.append(
            {
                "project_id": project.id,  # used in href links and static images paths
                "project_title": project.title,
                "project_desc": project.description,
                "project_category": project.category.name,
                "project_owner": project.owner.name,
                "project_owner_img": project.owner.profile_pic,
                "project_pic": project.projectpicture_set.all()[0],
                "project_pledged": project.total_target,
                "project_funded": 0,
                "project_time": 0,
            }
        )
    render_data = {
        "all_projects": projects_data_list
    }
    return render(request, "projects/view_projects.html", render_data)
