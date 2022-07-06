from rest_framework import serializers
from core.models import SmartCondition, Condition, SensorState
from api.serializers.sensor import SensorSerializer

class SensorStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorState
        fields = '__all__'

class ConditionSerializer(serializers.ModelSerializer):
    timer=serializers.TimeField(format='%H:%M')
    sensor_status = SensorStateSerializer()
    class Meta:
        model = Condition
        fields = '__all__'
        
class SmartConditionSerializer(serializers.ModelSerializer):
    condition = ConditionSerializer()
    class Meta:
        model = SmartCondition
        fields = '__all__'
        read_only_fields = ('id', 'created_at','owner')
