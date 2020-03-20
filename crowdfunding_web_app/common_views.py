from django.shortcuts import render


def render_404_page(request):
    return render(request, "crowdfunding_web_app/404/404.html")
