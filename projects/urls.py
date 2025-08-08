# projects/urls.py
from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('lacuna/', views.lacuna, name='lacuna'),
    path('blacklight/', views.blacklight, name='blacklight'),
    path('gradflow/', views.gradflow, name='gradflow'),
    path('afl/', views.afl, name='afl'),
    path('bonsai/', views.bonsai, name='bonsai'),
]