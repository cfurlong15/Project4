from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('projects/<int:project_id>/', views.projects_detail, name='detail'),
    path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='projects_delete'),
    path('projects/<int:project_id>/add_task/', views.add_task, name='add_task'),
    path('projects/<int:project_id>/edit_task/<int:pk>/', views.TaskUpdate.as_view(), name='tasks_update'),
    path('projects/<int:project_id>/delete_task/<int:task_id>/', views.tasks_delete, name='tasks_delete'),
]