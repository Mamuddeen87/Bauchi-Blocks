from django.db import models
from user.models import Profile

class CementRecord(models.Model):
    cement_company = models.CharField(max_length=30)
    cement_bought_from = models.CharField(max_length=30)
    cement_bags_bought = models.PositiveIntegerField()
    cement_bags_used = models.PositiveIntegerField()
    picked_by = models.ForeignKey(
            Profile,
            on_delete=models.CASCADE
            )
    date = models.DateTimeField()
    notes = models.TextField(
            blank=True,
            null=True
            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cement Record on {self.date}"
