from django.shortcuts import render
from .models import Project
# Create your views here.

# retorna la vista home


def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})
