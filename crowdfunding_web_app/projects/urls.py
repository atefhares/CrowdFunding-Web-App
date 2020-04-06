from django.urls import path

from projects.views import donate_project
from projects.views import view_project, list_projects, insert_update_project

urlpatterns = [
    path('', list_projects.handle_list_all_projects_request, name='list_projects'),
    path('create', insert_update_project.handle_create_new_project_request),
    path('update/<project_id>', insert_update_project.handle_update_project_request),
    path('<project_id>', view_project.handle_view_project_request, name='view_project'),
    path('<project_id>/donate', donate_project.donate_project),
    path('update', insert_update_project.handle_update_project_request),
    # path('<project_id>', view_project.handle_view_project_request,name="show_project"),
    # path('views/submit_comment',view_project.submit_comment, name="submit_comment"),
    path('submit_comment/<project_id>', view_project.submit_comment, name="submit_comment"),
    path('report_comment/<comment_id>', view_project.report_comment, name="report_comment")
]
