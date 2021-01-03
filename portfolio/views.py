from django.shortcuts import render
from .models import Image,Project
# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def skills(request):
    images = Image.objects.all()
    return render(request,"skills.html",{"images":images})

def projects(request):
    projects = Project.objects.all()
    return render(request,"projects.html",{"projects":projects})