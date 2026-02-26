from rest_framework.routers import DefaultRouter
from .serializers import EngineSerializer, ProductionRecordSerializer
from .views import EngineModelViewSet, ProductionRecordModelViewSet

router = DefaultRouter()
router.register(r'', EngineModelViewSet, basename="engine")
urlpatterns = router.urls

router = DefaultRouter()
router.register(r'', ProductionRecordModelViewSet, basename="production")
urlpatterns = router.urls
