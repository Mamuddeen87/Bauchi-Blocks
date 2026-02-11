from django.contrib import admin
from .models import Customer, Sale

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer", "block_type", "quantity", "total_amount", "payment_type", "date")
    search_fields = ("date", "block_type", "payment_type")

admin.site.register(Sale, CustomerAdmin)
