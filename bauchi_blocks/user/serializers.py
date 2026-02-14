from .models import Profile
from djangp_framework import serializer
from django.contrib.auth.models import user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        field = '__all__'
