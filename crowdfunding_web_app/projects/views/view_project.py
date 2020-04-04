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
    project = get_project(project_id)
    comment_num = project.comments.all().count()
    comments = project.comments.order_by('-created_at')
    context = {'project': get_project(project_id),'comment_num': comment_num,'comments': comments}
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
        else:
            if request.user.is_authenticated:
                user = request.user
                project = Project.objects.get(id = project_id)
                comment = Comment(
                    comment = comment_value,
                    project = project,
                    user = user,
                )
                comment.save()               
    return redirect('show_project',project_id)

@login_required(login_url='/accounts/login/')
def report_comment(request, comment_id):
    print(comment_id)
    comment = Comment.objects.get(id= comment_id)
    print(comment)
    project_id = comment.project.id
    if comment.is_reported == False and comment.user.email == request.user.email:
        comment.comment_reports += 1
        comment.is_reported = True
    else:
        comment.comment_reports += 1
        comment.save()
    comment.save() 
    return redirect('show_project', project_id)