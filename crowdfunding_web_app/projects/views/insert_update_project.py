from django.shortcuts import render
import re
from projects.models import Project, Category
from accounts.models import Country
from django_countries import countries
from django.contrib import messages


def handle_update_project_request(request):
    return None


def is_valid_description(title):
    return 5 <= len(title) <= 20 and re.search("^[a-zA-Z]+$", title)


def is_valid_title(title):
    return 5 <= len(title) <= 20 and re.search("^[a-zA-Z]+$", title)


def handle_create_new_project_request(request):
    print(request)
    print(request.POST)

    if request.method == "GET":
        all_categories = Category.objects.all()
        # all_countries = Country.objects.all()

        render_data = {
            "categories": all_categories,
            "countries": countries
        }
        return render(request, "projects/create_project.html", render_data)
    else:
        title = request.POST.get("title")
        description = request.POST.get("description")
        country = request.POST.get("country")
        category = request.POST.get("category")
        duration = request.POST.get("duration")

        if not is_valid_title(title):
            messages.error(request, 'Title is not valid!')

        if not is_valid_description(description):
            messages.error(request, 'Description is not valid!')

        return render(request, "projects/create_project.html")

        new_project = Project()
        new_project.title = request.POST.get("title")
