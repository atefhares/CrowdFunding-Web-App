from django.urls import path
from django.conf.urls import url
from projects.views import view_project, list_projects, insert_update_project

urlpatterns = [
    path('', list_projects.handle_list_all_projects_request, name='list_projects'),
    path('create', insert_update_project.handle_create_new_project_request),
    path('update', insert_update_project.handle_update_project_request),
    path('<project_id>', view_project.handle_view_project_request),
    # path('views/submit_comment',view_project.submit_comment, name="submit_comment"),
    path('submit_comment/<project_id>/', view_project.submit_comment, name="submit_comment"),
]
