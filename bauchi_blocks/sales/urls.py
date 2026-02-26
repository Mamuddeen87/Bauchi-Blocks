from django.urls import path
from .views import SalesList, SalesCreate, SalesUpdate, SalesDetail, SalesDelete, CustomerList, CustomerCreate, CustomerUpdate, CustomerDelete, CustomerDetail

urlpatterns = [
        path("", SalesList.as_view(), name="sales_list"),
        path("new/", SalesCreate.as_view(), name="sales_create"),
        path("update/<int:pk>/", SalesUpdate.as_view(), name="sales_update"),
        path("delete/<int:pk>/", SalesDelete.as_view(), name="sales_delete"),
        path("detail/<int:pk>/", SalesDetail.as_view(), name="sales_detail"),

        path("", CustomerList.as_view(), name="customer_list"),
        path("new/", CustomerCreate.as_view(), name="customer_create"),
        path("update/<int:pk>/", CustomerUpdate.as_view(), name="customer_update"),
        path("delete/<int:pk>/", CustomerDelete.as_view(), name="customer_delete"),
        path("detail/<int:pk>/", CustomerDetail.as_view(), name="customer_detail")

        ]
