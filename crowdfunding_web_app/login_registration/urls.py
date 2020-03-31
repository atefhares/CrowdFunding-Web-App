from django.urls import path
from . import views
urlpatterns = [
    path('templates/login', views.login, name='login'),
    path('register', views.register, name='register'),

]