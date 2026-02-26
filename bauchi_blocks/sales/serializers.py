from .models import Customer, Sale
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        field = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        field = '__all__'
