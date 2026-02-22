from django.urls import path
from .views import SandCreate, SandUpdate, SandList, SandDetail, SandDelete

urlpatterns = [
        path("", SandList.as_view(), name="sand_list"),
        path("new/", SandCreate.as_view(), name="sand_create"),
        path("update/<int:pk>/", SandUpdate.as_view(), name="sand_update"),
        path("detail/<int:pk>/", SandDetail.as_view(), name="sand_detail"),
        path("delete/<int:pk>/", SandDelete.as_view(), name="sand_delete")
        ]
