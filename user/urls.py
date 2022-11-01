from django.urls import path
from user import views

urlpatterns = [
    path('register', views.register_user, name="register"),
    path('login', views.login_request, name='login'),
    path('profile/', views.user_profile, name="user_profile"),
    path('log_out/', views.log_out, name="log_out"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         views.activate, name='activate'),
    path('edit/', views.edit_profile, name="edit_profile"),
    path('delete/', views.delete, name="delete"),

]
