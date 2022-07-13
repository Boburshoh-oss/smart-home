from rest_framework import serializers
from core.models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
        read_only_fields = ('owner','topic_name','created_at','updated_at')