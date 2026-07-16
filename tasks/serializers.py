from rest_framework import  serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'is_done',
            'created_at',
        ]
        read_only_fields = ['created_at']
