from rest_framework import serializers
from core.models import Device, Product, Home, Channel,Sensor


class DeviceSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        read_only=False,
        queryset=Product.objects.all(),
        slug_field='name'
    )
    home = serializers.SlugRelatedField(
        read_only=False,
        queryset=Home.objects.all(),
        slug_field='name'
    )
    
    channels = serializers.PrimaryKeyRelatedField(many=True, queryset=Channel.objects.all())
    sensors = serializers.PrimaryKeyRelatedField(many=True, queryset=Sensor.objects.all())
    class Meta:
        model = Device
        fields = '__all__'
        read_only_fields = ('owner',)
    
    
