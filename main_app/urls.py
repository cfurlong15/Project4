from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('projects/<int:project_id>/', views.projects_detail, name='detail'),
]