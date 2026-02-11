from django.contrib import admin
from .models import Engine, ProductionRecord

class ProductionAdmin(admin.ModelAdmin):
    list_display = ("engine", "operator", "deputy", "quantity_produced", "block_type", "date")
    search_fields = ("engine", "block_type", "operator")

admin.site.register(ProductionRecord, ProductionAdmin)

