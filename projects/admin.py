from django.contrib import admin
from .models import Category, Project, Donate, Comment, Rating, ProjectReport

# Register your models here.
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Donate)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(ProjectReport)
