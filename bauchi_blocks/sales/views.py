from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from .models import Customer, Sale
from .serializers import CustomerSerializer, SalesSerializer
from rest_framework.viewsets import ModelViewSet

class CustomerModelViewSet(ModelViewSet):
    queryset = Customer.objects.all() 
    serializer_class = CustomerSerializer

class SalesModelViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SalesSerializer

class CustomerList(ListView):
    model = Customer
    fields = ['name', 'phone', 'address']
    template_name = "sales/sales_list.html"
    success_url = "/"

class CustomerCreate(CreateView):
    model = Customer
    fields = ['name', 'phone', 'address']
    template_name = "sales/sales_create_update.html"

class CustomerUpdate(UpdateView):
    model = Customer
    fields = ['name', 'phone', 'address']
    template_name = "sales/sales_create_update.html"

class CustomerDetail(DetailView):
    model = Customer
    fields = ['name', 'phone', 'address']
    template_name = 'sales/sales_detail.html'

class CustomerDelete(DeleteView):
    model = Customer
    template_name = "sales/sales_delete.html"

class SalesList(ListView):
    model = Sale
    fields = ['customer', 'block_type', 'quantity', 'total_amount', 'payment_type', 'amount_paid', 'balance', 'entered_by']
    template_name = "sales/sales_list.html"
    success_url = "/"

class SalesCreate(CreateView):
    model = Sale
    fields = ['customer', 'block_type', 'quantity', 'total_amount', 'payment_type', 'amount_paid', 'balance', 'entered_by']
    template_name = "sales/sales_create_update.html"

class SalesUpdate(UpdateView):
    model = Sale
    fields =   ['customer', 'block_type', 'quantity', 'total_amount', 'payment_type', 'amount_paid', 'balance', 'entered_by']
    template_name = "sales/sales_create_update.html"

class SalesDetail(DetailView):
    model = Sale
    fields = ['customer', 'block_type', 'quantity', 'total_amount', 'payment_type', 'amount_paid', 'balance', 'entered_by']
    template_name = 'sales/sales_detail.html'

class SalesDelete(DeleteView):
    model = Sale
    template_name = "sales/sales_delete.html"
