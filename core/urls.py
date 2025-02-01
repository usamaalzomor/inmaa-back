from rest_framework.routers import DefaultRouter
from core.views import ServiceViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service')

urlpatterns = router.urls