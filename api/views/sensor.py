from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.serializers import SensorSerializer
from core.models.sensor import Sensor


class SensorListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()
            
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = Sensor.objects.filter(owner=user)
        else:
            queryset = Sensor.objects.all()
        return queryset

class SensorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()