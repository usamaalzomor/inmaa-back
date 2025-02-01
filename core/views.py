from rest_framework.viewsets import ReadOnlyModelViewSet
from core.models import Service
from core.serializers import ServiceSerializer

class ServiceViewSet(ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer