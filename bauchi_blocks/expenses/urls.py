from django.urls import path
from .views import ExpensesCreate, ExpensesDelete, ExpensesUpdate, ExpensesDetail, ExpensesList
urlpatterns = [
        path("", ExpensesList.as_view(), name="expenses_home"),
        path("new/", ExpensesCreate.as_view(), name="expenses_create"),
        path("delete/<int:pk>/", ExpensesDelete.as_view(), name="expenses_delete"),
        path("update/<int:pk>/", ExpensesUpdate.as_view(), name="expenses_update"),
        path("detail/<int:pk>/", ExpensesDetail.as_view(), name="expenses_detail")
        ]
