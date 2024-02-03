from django.urls import path
from .views import *



urlpatterns = [
    path('',home,name='home'),
    path('projectManagers/',projectManagersView,name="projectManagersView"),
    path('projects/',projectsView,name="projectsView")
    
]
