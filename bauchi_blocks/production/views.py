from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from .models import Engine, ProductionRecord
from .serializers import EngineSerializer, ProductionRecordSerializer
from rest_framework.viewsets import ModelViewSet

class EngineModelViewSet(ModelViewSet):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer

class ProductionRecordModelViewSet(ModelViewSet):
    queryset = ProductionRecord.objects.all()
    serializer_class = ProductionRecordSerializer

class EngineCreateView(CreateView):
    model = Engine 
    fields= ['name', 'description']
    template_name = "production/ProductionCreate.html"
    success_url = "/"

class EngineDeleteView(DeleteView):
    model = Engine
    fields = ['name', 'description']
    template_name = "production/ProductionDelete.html"
    success_url = "/"

class EngineUpdateView(UpdateView):
    model = Engine
    fields = ['name','description']
    template_name = "production/ProductionUpdate.html"
    success_url = "/"

class EngineListView(ListView):
    model = Engine
    template_name = "production/ProductionList.html"

class EngineDetailView(DetailView):
    model = Engine
    template_name = "Production/ProductionDetail.html"





class ProductionCreateView(CreateView):
    model = ProductionRecord
    fields= ['engine', 'operator', 'deputy', 'quantity_produced', 'block_type']
    template_name = "production/ProductionCreate.html"
    success_url = "/"

class ProductionDeleteView(DeleteView):
    model = ProductionRecord
    fields = ['engine', 'operator', 'deputy', 'quantity_produced', 'block_type']
    template_name = "production/ProductionDelete.html"
    success_url = "/"

class ProductionUpdateView(UpdateView):
    model = ProductionRecord
    fields = ['engine', 'operator', 'deputy', 'quantity_produced', 'block_type']
    template_name = "production/ProductionUpdate.html"
    success_url = "/"

class ProductionListView(ListView):
    model = ProductionRecord
    template_name = "production/ProductionList.html"

class ProductionDetailView(DetailView):
    model = ProductionRecord
    template_name = "Production/ProductionDetail.html"

