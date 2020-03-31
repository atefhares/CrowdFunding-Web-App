from django.shortcuts import render

from projects.models import Project, Category
from accounts.models import Country


def handle_update_project_request(request):
    return None


def handle_create_new_project_request(request):
    print(request)
    print(request.POST)
    if request.method == "GET":
        all_categories = Category.objects.all()
        # all_countries = Country.objects.all()

        render_data = {
            "categories": all_categories,
            # "countries": all_countries
        }
        return render(request, "projects/create_project.html", render_data)
    else:
        None
