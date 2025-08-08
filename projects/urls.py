# projects/urls.py
from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    # Research projects
    path('lacuna/', views.lacuna, name='lacuna'),
    path('blacklight/', views.blacklight, name='blacklight'),
    path('gradflow/', views.gradflow, name='gradflow'),
    path('afl/', views.afl, name='afl'),
    path('bonsai/', views.bonsai, name='bonsai'),
    # Interface projects (future subdomains)
    path('clinical/', views.clinical, name='clinical'),
    path('pharma/', views.pharma, name='pharma'),
    path('finance/', views.finance, name='finance'),
    path('insurance/', views.insurance, name='insurance'),
]