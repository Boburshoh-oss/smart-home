from rest_framework import serializers
from core.models import Device, Product, Home, Channel


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
    channels = serializers.SlugRelatedField(
        read_only=False,
        many=True,
        queryset=Channel.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Device
        fields = '__all__'
