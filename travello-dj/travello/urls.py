from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view



urlpatterns = [

    path('' , index , name='index'),
    path('contact' , contact , name='contact'),

    path('register' , register , name='register'),
    path('login' , auth_view.LoginView.as_view(template_name='login.html') , name='login'),
    path('logout' , auth_view.LogoutView.as_view(template_name='logout.html') , name='logout'),
    
]
