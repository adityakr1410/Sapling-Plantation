from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.


def home(request):
    return HttpResponse("<h2>Hello World</h2>")

def projectManagersView(request):
    managers = projectManager.objects.all()
    context={
        "managers":managers,    
    }
    return render(request,"test/projectManagers.html",context)


def projectsView(request):
    proj = projects.objects.all()
    context={
        "projects":proj
    }
    return render(request,"test/projects.html",context) 

