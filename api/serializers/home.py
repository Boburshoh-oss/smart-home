from rest_framework import serializers
from core.models import Home
from api.serializers import UserSerializer

class HomeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Home
        fields = "__all__"
        read_only_fields = ('created_at','owner')
