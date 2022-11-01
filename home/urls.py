from django.urls import path
from home.views import home,proj_category

urlpatterns = [
    path("", home, name="home"),
    path("<int:id>/category/projects", proj_category, name="proj_category"),

]
