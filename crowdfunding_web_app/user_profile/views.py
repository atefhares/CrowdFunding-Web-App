# from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm, UserDeleteForm, ProfileDeleteForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from accounts.models import UserProfile, User, Country, CountryField
from django.db.models import Sum
import datetime
from django.urls import reverse
from projects.models import Project


def profile(request):
    return render(request, 'user_profile/pro.html')


def edit_profile(request):
    print(request.user.email)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        user_form.fields['email'].disabled = True
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')


    else:
        user_form = UserUpdateForm(instance=request.user)
        user_form.fields['email'].disabled = True
        profile_form = ProfileUpdateForm(instance=request.user.user_profile)
    context = {
        'u_form': user_form,
        'p_form': profile_form

    }
    return render(request, "user_profile/edit.html", context)


def deleteuser(request):
    if request.method == 'GET':
        return render(request, "user_profile/delete.html")

        # deleteform=UserDeleteForm(request.POST,instance=user)
        # deletepform=ProfileDeleteForm(request.POST,
        #                               request.FILES,
        #                               instance=request.user.user_profile
        #
        #                              )
    else:

        request.user.user_profile.delete()
        request.user.delete()

        messages.info(request, 'Your account has been deleted.')
        return redirect('/')


def list_projects(request):
    if request.method == "GET":
        # userr = request.user.id
        # projects = userr.projects_set.all()
        user = Project.objects.filter(owner=request.user)
        print(user)
        projects_list = []
        for project in user:
            days = (datetime.date.today() - project.start_date).days
            project_time_1 = days
            project_time_2 = "days ago"
            if days == 0:
                project_time_1 = "today"
                project_time_2 = ""

            projects_list.append(
                {
                    "project_id": project.id,  # used in href links and static images paths
                    "project_title": project.title,
                    "project_desc": project.description,
                    "project_category": project.category.name,
                    "project_owner": project.owner.first_name,
                    "project_owner_img": project.owner.user_profile.profile_pic,
                    "project_pic": project.projectpicture_set.all()[:1].get().pic_path,
                    "project_pledged": project.total_target,
                    "project_funded": project.donation_set.aggregate(Sum('amount')).get('amount__sum'),
                    "project_time_1": project_time_1,
                    "project_time_2": project_time_2,
                    "project_start_date": project.start_date,
                    "project_end_date": project.end_date,
                }
            )
        context = {
            "all_projects": projects_list
        }
        return render(request, "user_profile/projects.html", context)
