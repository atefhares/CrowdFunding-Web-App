from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login,name='login'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    url(r'^activate/(?P<key>[0-9A-Za-z]{45})/$',views.activate, name='activate'),
    path('resend_activation_email/<email>',views.resend_activation_email,name='resend_activation_email'),   
    path('forget_password',views.forget_password,name='forget_password'),
    url(r'^reset_password/(?P<key>[0-9A-Za-z]{45})/$',views.reset_password, name='reset_password'),
    url(r'^submit_password_new_value/(?P<key>[0-9A-Za-z]{45})/$', views.submit_password_new_value,name='submit_password_new_value'),
]
