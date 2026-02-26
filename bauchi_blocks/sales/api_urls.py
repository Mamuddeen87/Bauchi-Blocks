from rest_framework.routers import DefaultRouter
from .serializers import CustomerSerializer, SalesSerializer
from .views import CustomerModelViewSet, SalesModelViewSet

router = DefaultRouter()
router.register(r'customer', CustomerModelViewSet, basename="customer_router")
urlpatterns = router.urls

router = DefaultRouter()
router.register(r'sales', SalesModelViewSet, basename="sales")
urlpatterns = router.urls
