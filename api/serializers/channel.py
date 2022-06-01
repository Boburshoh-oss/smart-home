from rest_framework import serializers
from core.models import Channel, Status, Device


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
