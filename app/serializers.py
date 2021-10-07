from app.models import TodoList

from rest_framework import serializers


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ['id', 'name', 'done', 'created_at']

