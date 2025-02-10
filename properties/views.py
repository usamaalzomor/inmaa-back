# properties/views.py

from rest_framework import viewsets
from .models import Property, PropertyImage
from django.db.models import Prefetch
from .serializers import PropertyListSerializer, PropertyDetailSerializer
from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters
from properties.filters import PropertyFilter

class PropertyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    The Main ViewSet for listing and retrieving properties.
    """

    filter_backends = (filters.DjangoFilterBackend, drf_filters.SearchFilter)
    search_fields = [ 'property_type__name', 'usage_type', 
                        'description', 'city__name', 'state__name'
                    ]
    filterset_class = PropertyFilter

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
