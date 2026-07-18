from django.urls import path
from .views import TaskListCreativeView, TaskDetailView


urlpatterns = [
    path('tasks/',TaskListCreativeView.as_view(), name='task_list'),
    path('tasks/<int:pk>/',TaskDetailView.as_view(), name='task_detail'),
]