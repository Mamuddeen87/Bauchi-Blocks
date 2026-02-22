from django.contrib import admin
from .models import SandRecord

class SandAdmin(admin.ModelAdmin):
    list_display = ("sand_quantity", "used_quantity", "picked_by", "created_at", "updated_at")
    search_fields = ("picked_by",)

admin.site.register(SandRecord, SandAdmin)

