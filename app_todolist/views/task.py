from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response

from app_todolist.models import Task
from app_todolist.serializers.task import TaskSerializer
from rest_framework.viewsets import ViewSet


class TaskAPIView(ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView,
                  generics.DestroyAPIView,
                  generics.UpdateAPIView):

    def get_serializer_class(self):
        return TaskSerializer

    def get_queryset(self):
        return Task.objects.all()

    @action(methods=['POST'], detail=True, url_path='completed')
    def set_task_completed(self, request, pk=None):
        obj = self.get_object()
        obj.is_completed = True
        obj.save()
        serializer = TaskSerializer(obj)

        return Response(serializer.data)

    @action(methods=['POST'], detail=True, url_path='uncompleted')
    def set_task_uncompleted(self, request, pk=None):
        obj = self.get_object()
        obj.is_completed = False
        obj.save()
        serializer = TaskSerializer(obj)

        return Response(serializer.data)