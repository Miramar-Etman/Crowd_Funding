from django.conf.urls.static import static
from django.urls import path

from Crowd_Funding import settings
from . import views


urlpatterns = [
    path('create_project', views.create_project, name='create_project'),
    path('show_projects', views.show_all, name='show_projects'),
    path('avaliable_proj', views.avaliable_all, name='avaliable_proj'),
    path('projects/<int:id>', views.single_project, name='single_proj'),
    path('donate/<int:id>', views.donate, name='donate'),
    path('cancel/<int:id>', views.cancel_project, name='cancel_project'),
    path('<int:pk>/comment', views.AddCommentView.as_view(), name='add_comment'),
    path('<int:pk>/rate', views.AddRateView, name='add_rate'),
    path('donations', views.donations, name='donations'),
    path('view_search', views.search_project, name='search'),
    path('<int:pk>/report_project', views.report_project, name='report_project'),
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
