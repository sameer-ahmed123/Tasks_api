from rest_framework import serializers
from ApiApp.models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="Task_title")

    class Meta:
        model = Tasks
        fields = [
            "id",
            'Task_title',
            'slug',
            'Task',
            'name'
        ]
