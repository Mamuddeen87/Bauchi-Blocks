from django.db import models
from user.models import Profile

class Engine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ProductionRecord(models.Model):
    BLOCK_CHOICES = [
            ('Six Inches (6")', 'Six Inches (6")'),
            ('Nine Inches (9")', 'Nine Inches (9)"'),
            ]

    engine = models.ForeignKey(
            Engine,
            on_delete = models.CASCADE
            )
    operator = models.ForeignKey(
            Profile,
            related_name = 'operations',
            on_delete=models.CASCADE
            )
    deputy = models.ForeignKey(
            Profile,
            related_name="entered_records",
            on_delete=models.CASCADE
            )
    quantity_produced = models.PositiveIntegerField()
    block_type = models.CharField(
            max_length=20,
            choices=BLOCK_CHOICES)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity_produced} of {self.block_type} was produced on {self.date}"
