"""Модуль администрирования для приложения API."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Docstring for TaskSerializer."""

    class Meta:
        """Docstring for TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
