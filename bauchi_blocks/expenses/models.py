from django.db import models
from user.models import Profile

class Expenses(models.Model):
    EXPENSE_TYPES = [
            ('materials', 'materials'),
            ('operators_stipend', 'operators_stipend')
            ]

    item_name = models.CharField(max_length=255)
    quantity_or_amount = models.DecimalField(
            max_digits=20,
            decimal_places=2
            )
    purchase_by = models.ForeignKey(
            Profile,
            on_delete=models.CASCADE,
            )
    expense_type = models.CharField(
            max_length=20,
            choices=EXPENSE_TYPES
            )
    date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.date} - {self.item_name} - {self.expense_type}"
