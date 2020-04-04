from django.shortcuts import render

# Create your views here.
from admins.models import FeaturedProject
from projects.models import Project, Category


def index(request):
    context = {'latest_featured_projects': get_latest_featured_projects(),
               'highest_rated_projects': get_highest_rated_projects(),
               'latest_projects': get_latest_projects(),
               'categories': get_categories_alphabetical()}


    print(context)
    return render(request, 'homepage/index.html', context=context)


def get_latest_featured_projects():
    latest_featured_projects = FeaturedProject.objects.order_by('-date_featured')
    return latest_featured_projects


def get_highest_rated_projects():
    # returns 5 projects based on rating by descending order
    highest_rated_projects = Project.objects.order_by('-project_rating')[:5]  # the '-' is for descending
    return highest_rated_projects


def get_latest_projects():
    # returns 5 latest 5 projects based on start_date
    latest_projects = Project.objects.order_by('-start_date')[:5]
    return latest_projects


def get_categories_alphabetical():
    categories = Category.objects.order_by('name')
    return categories
