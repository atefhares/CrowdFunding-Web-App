from django.conf import settings
from django.shortcuts import render, redirect
from projects.models import Project, Donation
from django.db.models import Sum
import math
import datetime


def donate_project(request, project_id):
    if request.user.is_anonymous:
        return redirect('login')

    if not request.method == "POST":
        return redirect('404')

    project = Project.objects.get(id=project_id)
    if not project:
        return redirect('404')

    requested_donation = request.POST['donation']
    print("requested_donation: ", requested_donation)
    donation = Donation()
    donation.project = project
    donation.amount = requested_donation
    donation.user = request.user
    donation.save()
    
    return redirect('view_project', project_id=project_id)
