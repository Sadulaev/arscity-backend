from rest_framework import serializers
from .models import WorkExample

class WorkExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExample
        fields = '__all__'