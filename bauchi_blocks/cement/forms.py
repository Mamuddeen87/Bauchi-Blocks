from django import forms
from .models import CementRecord

class CementRecordForm(forms.ModelForm):
    class Meta:
        model = CementRecord
        fields = ["cement_company", "cement_bought_from", "cement_bags_bought", "cement_bags_used", "picked_by", "notes"]

