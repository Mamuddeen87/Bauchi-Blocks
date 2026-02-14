from .models import Expenses
from rest_framework import serializers

class ExpensesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        field = '__all__'
