from rest_framework.routers import DefaultRouter
from .views import SandViewSet

router = DefaultRouter()
router.register(r'sand', SandViewSet, basename="sand_router")
urlpatterns = router.urls


