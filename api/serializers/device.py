from rest_framework import serializers
from core.models import Device, Product, Home, Channel,Sensor


class DeviceSerializer(serializers.ModelSerializer):
    
    channels = serializers.PrimaryKeyRelatedField(many=True, queryset=Channel.objects.all(),required=False)
    sensors = serializers.PrimaryKeyRelatedField(many=True, queryset=Sensor.objects.all(),required=False)
    class Meta:
        model = Device
        fields = '__all__'
        read_only_fields = ('owner','channels','sensors')
    
    
