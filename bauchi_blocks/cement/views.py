from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import CementRecord
from .forms import CementRecordForm


class CementCreateView(CreateView):
    model = CementRecord
    template_name = "cement/cement_record.html"
    fields = ["cement_company", "cement_bought_from", "cement_bags_bought", "cement_bags_used", "picked_by", "notes"]


class CementDetailView(DetailView):
    model = CementRecord
    template_name = "cement/cement_record.html"

