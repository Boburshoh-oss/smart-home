from rest_framework import serializers
from core.models import Home
from api.serializers import UserSerializer

class HomeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Home
        fields = ['name','created_at','owner']
        read_only_fields = ('id', 'created_at','owner')
