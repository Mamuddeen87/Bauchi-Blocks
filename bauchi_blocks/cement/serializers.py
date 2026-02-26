from .models import CementRecord
from rest_framework import serializers

class CementRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CementRecord
        fields = '__all__'
