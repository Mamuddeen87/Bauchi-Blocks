from django.db import models
from user.models import Profile

class SandRecord(models.Model):
    sand_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    used_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    picked_by = models.ForeignKey(
            Profile, 
            on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sand Record on {self.date}"

