from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.http import HttpResponse
from projects.models import Project,Comment
from django.contrib.auth.decorators import login_required


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
    context = {}

    return render(request, "projects/project_details.html", context)




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
            messages.error(request,"Comment Can't Be Empty!")
            return render(request,'projects/project_details.html')
        else:
            if request.user.is_authenticated:
                user = request.user
                print(request.user)
            return render(request,'projects/project_details.html')
    else:
        return render(request,'projects/project_details.html')
