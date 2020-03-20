from django.urls import path
from projects.views import view_project, list_projects

urlpatterns = [
    path('', list_projects.handle_list_all_projects_request),
    path('<project_id>', view_project.handle_view_project_request),
]
