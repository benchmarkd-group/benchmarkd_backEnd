from rest_framework_mongoengine import serializers

from .models import Course

class CourseSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Course
        fields = '__all__'
