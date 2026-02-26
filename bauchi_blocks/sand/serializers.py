from .models import SandRecord
from rest_framework import serializers

class SandRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SandRecord
        fields = '__all__'
