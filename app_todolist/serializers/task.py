from rest_framework import serializers

from app_todolist.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'is_completed', 'created_date', 'updated_date', 'created_by', 'due_date',
                  'updated_by']

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.email)
        instance.description = validated_data.get('description', instance.content)
        instance.is_completed = validated_data.get('is_completed', instance.created)
        return instance
