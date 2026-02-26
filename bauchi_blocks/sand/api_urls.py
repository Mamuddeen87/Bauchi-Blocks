from rest_framework.routers import DefaultRouter
from .views import SandViewSet

router = DefaultRouter()
router.register(r'', SandViewSet, basename="sand")
urlpatterns = router.urls


