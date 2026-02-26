from .models import Expenses
from rest_framework import serializers

class ExpensesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'
