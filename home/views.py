from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render, redirect

from projects.models import Project, Category


def home(request):
    highest_rated_projects = Project.objects.annotate(avg_rate=Avg('ratings__scale')).order_by('-avg_rate')[:5]
    latest = Project.objects.order_by('-create_date')[:5]
    projects_admin = Project.objects.filter(is_featured=1)
    categories = Category.objects.all()
    context = {"highest_rated_projects":highest_rated_projects, "latest":latest,'projects_admin':projects_admin,"categories":categories}
    return render(request,"home/home.html",context)


def proj_category(request,id):
    projects = Project.objects.filter(Category_id=id)
    category = Category.objects.filter(id=id).values
    context = {"projects":projects,"category":category}
    return render(request,"home/project_category.html",context)
