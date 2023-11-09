"""
Definition of urls for TelegramBot.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('accounts/login/', views.login, name='login'), 
         
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    
    path('api/data/', views.get_data, name='get_data'),
    path('api/GetProgressbar/', views.Get_ProgressbarStatus, name='GetProgress_bar'),
    path('api/PostProgressbar/', views.Post_ProgressbarStatus, name='PostProgress_bar'),
    
]

""" LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ), is origin, use instead views.login"""