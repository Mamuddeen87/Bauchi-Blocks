from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import CementRecord
from .forms import CementRecordForm


class CementCreateView(CreateView):
    model = CementRecord
    template_name = "cement/cement_new.html"
    fields = ["cement_company", "cement_bought_from", "cement_bags_bought", "cement_bags_used", "picked_by", "notes"]


class CementDetailView(DetailView):
    model = CementRecord
    template_name = "cement/cement_record.html"
    fields = "__all__"

class CementListView(ListView):
    model = CementRecord
    template_name = "cement/cement_list.html"
