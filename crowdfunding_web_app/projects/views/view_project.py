import datetime
import math

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect

from projects.models import Project, Comment


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
    # project = get_project(project_id)
    # comment_num = project.comments.all().count()
    # comments = project.comments.order_by('-created_at')
    # context = {'project': get_project(project_id), 'comment_num': comment_num, 'comments': comments}
    # print(context)
    # return render(request, "projects/project_details.html", context)

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
        "comment_num": project.comments.all().count(),
        'comments': project.comments.order_by('-created_at'),
    }

    if project.donations.all().count() > 0:
        render_data["donations_list"] = project.donations.all()

    return render(request, "projects/project_details.html", render_data)


# def get_project(id):
#     project = Project.objects.get(id=id)
#     return project
#     context = {}
#
#     return render(request, "projects/project_details.html", context)


###################Comments################################

# all_comments = Project.comments
# context = {
#     "all_comments" : all_comments,
# }


@login_required(login_url='/accounts/login/')
def submit_comment(request, project_id):
    if request.method == 'POST':
        comment_value = request.POST['comment']
        if comment_value == '':
            messages.error(request, "Comment Can't Be Empty!")
        else:
            if request.user.is_authenticated:
                user = request.user
                project = Project.objects.get(id=project_id)
                comment = Comment(
                    comment=comment_value,
                    project=project,
                    user=user,
                )
                comment.save()
    return redirect('view_project', project_id)


@login_required(login_url='/accounts/login/')
def report_comment(request, comment_id):
    print(comment_id)
    comment = Comment.objects.get(id=comment_id)
    print(comment)
    project_id = comment.project.id
    if comment.is_reported == False and comment.user.email == request.user.email:
        comment.comment_reports += 1
        comment.is_reported = True
    else:
        comment.comment_reports += 1
        comment.save()
    comment.save()
    return redirect('view_project', project_id)
