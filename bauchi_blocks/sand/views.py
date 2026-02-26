from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import SandRecord
from rest_framework.viewsets import ModelViewSet
from .serializers import SandRecordSerializer

class SandViewSet(ModelViewSet):
    queryset = SandRecord.objects.all()
    serializer_class = SandRecordSerializer

class SandCreate(CreateView):
    model = SandRecord
    fields = ['sand_quantity', 'used_quantity', 'picked_by', 'notes']
    template_name = "sand/sand_create_update.html"
    success_url = "/"

class SandUpdate(UpdateView):
    model = SandRecord
    fields = ['sand_quantity', 'used_quantity', 'picked_by', 'notes']
    template_name = "sand/sand_create_update.html"
    success_url = "/"

class SandList(ListView):
    model = SandRecord
    fields = ['sand_quantity', 'used_quantity', 'picked_by', 'notes']
    template_name = "sand/sand_list.html"

class SandDetail(DetailView):
    model = SandRecord
    fields = ['sand_quantity', 'used_quantity', 'picked_by', 'notes']
    template_name = "sand/sand_detail.html"

class SandDelete(DeleteView):
    model = SandRecord
    fields = ['sand_quantity', 'used_quantity', 'picked_by', 'notes']
    template_name = "sand/sand_delete.html"
    success_url = "/"
