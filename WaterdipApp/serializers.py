from rest_framework import serializers
from .models import TaskTable

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskTable
        fields = ('id','title','is_completed')