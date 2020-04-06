from django.conf import settings
from django.shortcuts import render, redirect
from projects.models import Project
from django.db.models import Sum
import math
import datetime


def get_project_amount_view(target):
    if not target:
        return 0
    elif 1000 <= target < 1000000:
        return str(math.ceil(target / 1000)) + " K"
    # elif 100000 <= target < 1000000:
    #     return str(math.ceil(target / 100000)) + " KK"
    elif target > 1000000:
        return str(math.ceil(target / 1000000)) + " M"


def handle_view_project_request(request, project_id):
    if not request.method == "GET":
        return redirect('404')

    if settings.DEBUG:
        print("request: ", request)
        print("project_id: ", project_id)

    if request.user.is_anonymous:
        return redirect('login')

    try:
        project = Project.objects.get(id=project_id)
    except Exception:
        return redirect('404')

    if project.donations.all().count() == 0:
        donations = 0
    else:
        donations = project.donations.aggregate(Sum('amount')).get('amount__sum')

    days = (datetime.date.today() - project.start_date).days
    project_time_1 = days
    if days == 0:
        project_time_1 = "today"
        project_time_2 = ""
    elif days == 1:
        project_time_2 = "day ago"
    else:
        project_time_2 = "days ago"

    if donations < math.ceil(project.total_target):
        project_needs_donations = True
    else:
        project_needs_donations = False

    render_data = {
        "project_id": project.id,
        "project_title": project.title,
        "project_category": project.category.name,
        "project_images": project.pictures.all(),
        "project_description": project.description,
        "project_owner": project.owner,
        "project_owner_img": project.owner.user_profile.profile_pic,
        "project_pledged": get_project_amount_view(math.ceil(donations)),
        "project_funded": math.ceil(donations / project.total_target * 100),
        "project_total_target": get_project_amount_view(math.ceil(project.total_target)),
        "project_donations_count": project.donations.count(),
        "project_time_1": project_time_1,
        "project_time_2": project_time_2,
        "project_needs_donations": project_needs_donations,
        "max_donations_remains": math.ceil(project.total_target) - donations,
    }

    if project.donations.all().count() > 0:
        render_data["donations_list"] = project.donations.all()

    return render(request, "projects/project_details.html", render_data)
