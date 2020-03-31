from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
import re
from projects.models import Project, Category, ProjectPicture
from accounts.models import Country
from django_countries import countries
from django.contrib import messages
import datetime
from datetime import timedelta


def handle_update_project_request(request):
    return None


def is_valid_description(desc):
    return 20 <= len(desc) <= 200 and re.search("^[a-zA-Z]+$", desc)


def is_valid_title(title):
    return 5 <= len(title) <= 50 and re.search("^[a-zA-Z]+$", title)


def is_valid_duration(duration):
    return re.search("^[0-9]+$", duration) and int(duration) <= 365


def get_create_project_render_data():
    all_categories = Category.objects.all()
    # all_countries = Country.objects.all()
    render_data = {
        "categories": all_categories,
        "countries": countries
    }
    return render_data


def handle_create_new_project_request(request):
    print(request)
    print(request.POST)
    print(request.FILES)

    if request.user.is_anonymous:
        return redirect('login')

    if request.method == "GET":
        return render(request, "projects/create_project.html", get_create_project_render_data())
    else:
        title = request.POST.get("title")
        description = request.POST.get("description")
        country = request.POST.get("country")
        category = request.POST.get("category")
        duration = request.POST.get("duration")

        error_detected = False
        if not is_valid_title(title):
            messages.error(request, 'Invalid Title [min_length: 5, max_length: 20, no digits]')
            error_detected = True

        if not is_valid_description(description):
            messages.error(request, 'Invalid Description [min_length: 20, max_length: 200]')
            error_detected = True

        if not is_valid_duration(duration):
            messages.error(request, 'Invalid Duration [No text, max_value: 365]')
            error_detected = True

        if not request.FILES['ImageUpload']:
            messages.error(request, 'Need to select at least one project image')
            error_detected = True

        if error_detected:
            return render(request, "projects/create_project.html", get_create_project_render_data())
        else:
            new_project = Project()
            new_project.owner = User.objects.get(request.user.id)
            new_project.title = title
            new_project.description = description
            new_project.category = Category.objects.get(id=int(category))
            new_project.country = country
            new_project.start_date = datetime.date.today()
            new_project.end_date = datetime.date.today() + timedelta(days=int(duration))
            new_project.save()

            print(new_project)

            images = request.FILES.getlist('ImageUpload')
            fs = FileSystemStorage()
            for file in images:
                filename = fs.save(file.name, file)
                uploaded_file_url = fs.url(filename)
                project_pic = ProjectPicture()
                project_pic.project = new_project
                project_pic.pic_path = uploaded_file_url
                project_pic.save()

            redirect('list_projects')
