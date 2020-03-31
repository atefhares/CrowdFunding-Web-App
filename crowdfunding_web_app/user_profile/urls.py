from django.urls import path
from . import views

urlpatterns = [
    path('<id>', views.view_profile),

]
