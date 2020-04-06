from django.conf import settings
from django.db.models import Sum, Count
from django.shortcuts import render
import datetime
import math

from admins.models import FeaturedProject
from projects.models import Project
from projects.views.view_project import get_project_amount_view


def handle_list_all_projects_request(request):
    if settings.DEBUG:
        print("request: ", request)

    if request.method == "GET":
        all_projects = Project.objects.all()

        projects_data_list = get_project_data_for_view(all_projects)
        # if settings.DEBUG:
        # print("all_projects: ", all_projects)
        render_data = {
            "all_projects": projects_data_list
        }
        return render(request, "projects/view_projects.html", render_data)


def get_project_data_for_view(model):
    projects_data_list = []
    for project in model:
        if isinstance(project, FeaturedProject):
            project = project.project
        days = (datetime.date.today() - project.start_date).days
        project_time_1 = days

        if days == 0:
            project_time_1 = "today"
            project_time_2 = ""
        elif days == 1:
            project_time_2 = "day ago"
        else:
            project_time_2 = "days ago"

        if project.donations.all().count() == 0:
            donations = 0
        else:
            donations = math.ceil(
                project.donations.aggregate(Sum('amount')).get('amount__sum'))

        projects_data_list.append(
            {
                "project_id": project.id,  # used in href links and static images paths
                "project_title": project.title,
                "project_desc": project.description,
                "project_category": project.category.name,
                "project_country": project.country.name,
                "project_owner": project.owner.get_full_name(),
                "project_owner_img": project.owner.user_profile.profile_pic,
                "project_pic": project.pictures.first().pic_path,
                "project_num_of_backers": project.donations.count(),
                "project_pledged": get_project_amount_view(math.ceil(donations)),
                "project_funded": math.ceil(donations / project.total_target * 100),
                "project_time_1": project_time_1,
                "project_time_2": project_time_2,
                "project_start_date": project.start_date,
                "project_end_date": project.end_date,
            }
        )
    return projects_data_list
