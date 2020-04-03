from django.conf import settings
from django.db.models import Sum
from django.shortcuts import render
import datetime
from datetime import timedelta
from projects.models import Project


def handle_list_all_projects_request(request):
    if settings.DEBUG:
        print("request: ", request)

    if request.method == "GET":

        all_projects = Project.objects.all()

        # if settings.DEBUG:
        # print("all_projects: ", all_projects)
        projects_data_list = []

        for project in all_projects:
            days = (datetime.date.today() - project.start_date).days
            project_time_1 = days

            if days == 0:
                project_time_1 = "today"
                project_time_2 = ""
            elif days == 1:
                project_time_2 = "day ago"
            else:
                project_time_2 = "days ago"

            projects_data_list.append(
                {
                    "project_id": project.id,  # used in href links and static images paths
                    "project_title": project.title,
                    "project_desc": project.description,
                    "project_category": project.category.name,
                    "project_owner": project.owner.first_name,
                    "project_owner_img": project.owner.userprofile.profile_pic,
                    "project_pic": project.projectpicture_set.all()[:1].get().pic_path,
                    "project_pledged": project.total_target,
                    "project_funded": project.donation_set.aggregate(Sum('amount')).get('amount__sum'),
                    "project_time_1": project_time_1,
                    "project_time_2": project_time_2,
                    "project_start_date": project.start_date,
                    "project_end_date": project.end_date,
                }
            )
        render_data = {
            "all_projects": projects_data_list
        }
        return render(request, "projects/view_projects.html", render_data)
