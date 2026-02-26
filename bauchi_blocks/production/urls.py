from django.urls import path
from .views import ProductionCreateView, ProductionListView, ProductionDeleteView, ProductionUpdateView, ProductionDetailView

urlpatterns = [
        path('', ProductionListView.as_view(), name="list"),
        path('new/', ProductionCreateView.as_view(), name="create"),
        path('delete/<int:pk>/', ProductionDeleteView.as_view(), name="delete"),
        path('update/<int:pk>/', ProductionUpdateView.as_view(), name="update"),
        path('detail/<int:pk>/', ProductionDetailView.as_view(), name="detail")
        ]
