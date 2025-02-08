# properties/views.py

from rest_framework import viewsets
from .models import Property, PropertyImage
from django.db.models import Prefetch
from .serializers import PropertyListSerializer, PropertyDetailSerializer

class PropertyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing and retrieving properties.
    """
    queryset = Property.objects.prefetch_related(
    Prefetch(
        'images',
        queryset=PropertyImage.objects.filter(is_main=True),
        to_attr='main_images'
        )
    )

    def get_serializer_class(self):
        if self.action == 'list':
            return PropertyListSerializer
        return PropertyDetailSerializer
