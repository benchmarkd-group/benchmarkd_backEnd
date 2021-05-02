from rest_framework_mongoengine import serializers

from .models import Institute

class InstiSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Institute
        fields = '__all__'