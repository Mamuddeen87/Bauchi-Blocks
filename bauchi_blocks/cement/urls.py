from django.urls import path
from .views import CementDetailView, CementCreateView, CementListView
from django.contrib.auth import views as auth_views

urlpatterns = [
        path("", CementListView.as_view(), name="cement_list"),
        path("new/", CementCreateView.as_view(), name="cement_new"),        
        path("<int:pk>", CementDetailView.as_view(), name="cement_record")
        ]
