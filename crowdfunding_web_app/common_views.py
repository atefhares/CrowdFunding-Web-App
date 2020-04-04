from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic import ListView

from projects.models import Project


def render_404_page(request):
    return render(request, "crowdfunding_web_app/404/404.html")


def logout_view(request):
    logout(request)
    return render(request, "homepage/index.html")


class SearchResultsView(ListView):
    model = Project
    template_name = 'crowdfunding_web_app/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Project.objects.filter(
            Q(title__icontains=query) | Q(category__name__icontains=query)
        ).distinct()
        return object_list

        # queryset = []
        # queries = query.split(" ")
        # for query in queries:
        #     projects = Project.objects.filter(
        #         Q(title__icontains=query) |
        #         Q(category__name__icontains=query)
        #     ).distinct()
        #
        #     for project in projects:
        #         queryset.append(project)
        #
        #     return list(set(queryset))
