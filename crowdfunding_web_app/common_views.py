from django.shortcuts import render
from django.contrib.auth import logout


def render_404_page(request):
    return render(request, "crowdfunding_web_app/404/404.html")


def logout_view(request):
    logout(request)
    return render(request, "homepage/index.html")


def not_found(request):
    return render(request, "crowdfunding_web_app/404/404.html")
