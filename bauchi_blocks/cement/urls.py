from django.urls import path
from .views import CementDetailView, CementCreateView, CementListView, CementUpdateView, CementDeleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
        path("", CementListView.as_view(), name="cement_list"),
        path("new/", CementCreateView.as_view(), name="cement_create"),        
        path("detail/<int:pk>/", CementDetailView.as_view(), name="cement_detail"),
        path("update/<int:pk>/", CementUpdateView.as_view(), name="cement_update"),
        path("delete/<int:pk>/", CementDeleteView.as_view(), name="cement_delete")
        ]
