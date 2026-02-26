from rest_framework.routers import DefaultRouter
from .serializers import ExpensesSerializers
from .views import ExpensesModelViewSet

router = DefaultRouter()
router.register(r'', ExpensesModelViewSet, basename="expenses")
urlpatterns = router.urls
