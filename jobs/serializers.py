from  rest_framework import serializers
from .models import JobPost

class JobPostSerializer(serializers.ModelSerializer):
    posted_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = JobPost
        fields = '__all__'
        ready_only_fields = ['posted_by', 'created_at']