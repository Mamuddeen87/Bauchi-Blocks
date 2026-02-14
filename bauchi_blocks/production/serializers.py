from .models import Engine, ProductionRecord
from rest_framework import serializers

class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        field = '__all__'

class ProductionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionRecord
        field = '__all__'
