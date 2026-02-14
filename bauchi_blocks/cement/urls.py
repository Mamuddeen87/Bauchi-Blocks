from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path("/<int:pk>", views.CementDetailView.as_view(), name="cement_record"),
        path("/new/", views.CementCreateView.as_view(), name="cement_record"),        
        ]
