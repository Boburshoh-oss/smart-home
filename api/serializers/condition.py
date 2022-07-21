from rest_framework import serializers
from core.models import SmartCondition, Condition, SensorState
from drf_writable_nested.serializers import WritableNestedModelSerializer

class SensorStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorState
        fields = '__all__'

class ConditionSerializer(WritableNestedModelSerializer):
    timer=serializers.TimeField(format='%H:%M',default=None)
    sensor_status = SensorStateSerializer(default=None)
    class Meta:
        model = Condition
        fields = '__all__'
        
class SmartConditionSerializer(WritableNestedModelSerializer):
    condition = ConditionSerializer()
    class Meta:
        model = SmartCondition
        fields = '__all__'
        read_only_fields = ('id', 'created_at','owner')
