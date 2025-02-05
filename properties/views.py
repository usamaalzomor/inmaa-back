# properties/views.py

from rest_framework import viewsets
from .models import Property
from .serializers import PropertyListSerializer, PropertyDetailSerializer

class PropertyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing and retrieving properties.
    """
    queryset = Property.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PropertyListSerializer
        return PropertyDetailSerializer
