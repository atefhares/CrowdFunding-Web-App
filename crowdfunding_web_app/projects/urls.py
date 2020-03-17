from django.urls import path
from projects.views import view_project

urlpatterns = [
    # path('', ),
    path('<project_id>', view_project.handle_view_project_request),
]