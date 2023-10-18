from rest_framework import generics

from app_todolist.models import Task
from app_todolist.serializers.task import TaskSerializer
from rest_framework.viewsets import ViewSet


class TaskAPIView(ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView, generics.DestroyAPIView,
                  generics.UpdateAPIView):

    def get_serializer_class(self):
        return TaskSerializer

    def get_queryset(self):
        return Task.objects.all()
