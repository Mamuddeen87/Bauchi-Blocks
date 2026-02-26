from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from .models import Expenses
from .serializers import ExpensesSerializers
from rest_framework.viewsets import ModelViewSet

class ExpensesModelViewSet(ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializers

class ExpensesCreate(CreateView):
    model = Expenses
    fields = ["item_name", "quantity_or_amount", "purchase_by", "expense_type", "date", "description"]
    template_name = "expenses/expenses_create.html"
    success_url = "/"

class ExpensesDelete(DeleteView):
    model = Expenses
    fields = ["item_name", "quantity_or_amount", "purchase_by", "expense_type", "date", "description"]
    success_url = "/"
    template_name = "expenses/expenses_delete.html"

class ExpensesUpdate(UpdateView):
    model = Expenses
    fields = ["item_name", "quantity_or_amount", "purchase_by", "expense_type", "date", "description"]
    template_name = "expenses/expenses_update.html"
    success_url = "/"

class ExpensesDetail(DetailView):
    model = Expenses
    template_name = "expenses/expenses_detail.html"

class ExpensesList(ListView):
    model = Expenses
    template_name = "expenses/expenses_list.html"
    context_object_name = "expenses_home"
