from rest_framework import serializers
from core.models import Home


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'
        read_only_fields = ('id', 'created_at',)
