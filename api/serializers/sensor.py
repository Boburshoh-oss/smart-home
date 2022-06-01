from rest_framework import serializers
from core.models import Sensor, Room


class SensorSerializer(serializers.ModelSerializer):
    room = serializers.SlugRelatedField(
        read_only=False,
        queryset=Room.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Sensor
        fields = '__all__'
