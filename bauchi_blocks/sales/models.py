from django.db import models
from user.models import Profile
from production.models import ProductionRecord

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Sale(models.Model):
    PAYMENT_CHOICES = [
            ('cash', 'cash'),
            ('credit', 'credit'),
            ('deposit', 'deposit')
            ]
    customer = models.ForeignKey(
            Customer,
            on_delete = models.CASCADE)
    block_type = models
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(
            max_digits=20, 
            decimal_places=2
            )
    total_amount = models.DecimalField(
            max_digits=20, 
            decimal_places=2, 
            blank=True
            )
    payment_type = models.CharField(
            max_length=10,
            choices=PAYMENT_CHOICES
            )
    amount_paid = models.DecimalField(
            max_digits=20,
            decimal_places=2
            )
    balance = models.DecimalField(
            max_digits=12,
            decimal_places=2,
            blank=True
            )
    entered_by=models.ForeignKey(
            Profile,
            on_delete=models.CASCADE,
            )
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.quantity * self.unit_price
        self.balance = self.total_amount - self.amount_paid
        super().save(*args, **kwargs)

    def __str__(self):
        return f"sale to {self.customer.name} on {self.date} at N{self.total_amount}"
