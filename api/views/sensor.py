from rest_framework import viewsets

from api.serializers import SensorSerializer
from core.models import Sensor


class SensorViewSet(viewsets.ModelViewSet):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()
