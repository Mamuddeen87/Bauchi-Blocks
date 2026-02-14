from .models import CaolinRecord
from rest_framework import serializers

class CaolinRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaolinRecord
        field = '__all__'
