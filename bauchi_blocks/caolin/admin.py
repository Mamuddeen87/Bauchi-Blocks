from django.contrib import admin
from .models import CaolinRecord

class CaolinAdmin(admin.ModelAdmin):
    list_display = ("picked_by", "date")
    search_fields = ("date", "picked_by")

admin.site.register(CaolinRecord, CaolinAdmin)
