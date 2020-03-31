from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    url(r'^activate/(?P<key>[0-9A-Za-z]{45})/$',views.activate, name='activate'),   
]
