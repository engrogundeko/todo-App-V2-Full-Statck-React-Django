from rest_framework import serializers
from .models import Task


class TaskList(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','name', 'description', 'date', 'status', 'user')