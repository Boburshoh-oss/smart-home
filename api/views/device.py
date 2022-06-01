from rest_framework import viewsets

from api.serializers import DeviceSerializer
from core.models import Device


class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
