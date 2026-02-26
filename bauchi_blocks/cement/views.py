from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import CementRecord
from .forms import CementRecordForm
from rest_framework.viewsets import ModelViewSet
from .serializers import CementRecordSerializer

class CementViewSet(ModelViewSet):
    queryset = CementRecord.objects.all()
    serializer_class = CementRecordSerializer

class CementCreateView(CreateView):
    model = CementRecord
    template_name = "cement/cement_new.html"
    fields = ["cement_company", "cement_bought_from", "cement_bags_bought", "cement_bags_used", "picked_by", "notes"]
    success_url = "/"


class CementDetailView(DetailView):
    model = CementRecord
    template_name = "cement/cement_detail.html"
    fields = "__all__"

class CementListView(ListView):
    model = CementRecord
    template_name = "cement/cement_list.html"

class CementUpdateView(UpdateView):
    model = CementRecord
    template_name = "cement/cement_update.html"
    fields = "__all__"

class CementDeleteView(DeleteView):
    model = CementRecord
    template_name = "cement/cement_delete.html"
    fields = "__all__"
