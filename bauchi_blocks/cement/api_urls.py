from rest_framework.routers import DefaultRouter
from .serializers import CementRecordSerializer
from .views import CementViewSet

router = DefaultRouter()
router.register(r'', CementViewSet, basename="cement")
urlpatterns = router.urls
