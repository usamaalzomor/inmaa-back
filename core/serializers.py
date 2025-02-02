from rest_framework import serializers
from core.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Service
        fields = ['id', 'name', 'icon']