from rest_framework.routers import DefaultRouter
from .serializers import CustomerSerializer, SalesSerializer
from .views import CustomerModelViewSet, SalesModelViewSet

router = DefaultRouter()
router.register(r'', CustomerModelViewSet, basename="customer")
urlpatterns = router.urls

router = DefaultRouter()
router.register(r'', SalesModelViewSet, basename="sales")
urlpatterns = router.urls
