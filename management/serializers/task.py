from rest_framework import serializers
from management.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'assigned_to',
            'project',
            'due_date',
            'is_completed',
            'created_at',
            'updated_at',
            'completed_tasks',
            'total_tasks',
        ]