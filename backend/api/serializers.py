"""settings serializers api."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """class settings serializers."""

    class Meta:
        """meta class serializers."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
