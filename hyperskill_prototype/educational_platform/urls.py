from django.urls import path

from . import views

app_name = 'educational_platform'
urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.TaskListView.as_view(), name='tasks'),
    path('tasks/<int:pk>', views.TaskDetailView.as_view(), name='task-detail'),
]
