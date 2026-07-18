from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Task
from .serializers import TaskSerializer


class TaskListCreativeView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer