from django.contrib import admin
from .models import Expenses

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("item_name", "quantity_or_amount", "purchase_by", "expense_type")
    search_fields = ("date", "expense_type", "purchase_by")

admin.site.register(Expenses, ExpenseAdmin)

