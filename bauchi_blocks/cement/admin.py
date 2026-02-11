from django.contrib import admin
from .models import CementRecord

class CementAdmin(admin.ModelAdmin):
    list_display = ("cement_bought_from", "cement_bags_bought", "cement_bags_used", "picked_by", "date", "notes", "created_at", "updated_at")
    search_fields = ("date", "picked_by")

admin.site.register(CementRecord, CementAdmin)

