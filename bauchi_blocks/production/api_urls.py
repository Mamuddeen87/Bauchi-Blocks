from rest_framework.routers import DefaultRouter
from .serializers import EngineSerializer, ProductionRecordSerializer
from .views import EngineModelViewSet, ProductionRecordModelViewSet

router = DefaultRouter()
router.register(r'engine', EngineModelViewSet, basename="engine_router")
urlpatterns = router.urls

router = DefaultRouter()
router.register(r'production', ProductionRecordModelViewSet, basename="production")
urlpatterns = router.urls
