from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.serializers import DeviceSerializer
from core.models.device import Device


class DeviceListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
            
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = Device.objects.filter(owner=user)
        else:
            queryset = Device.objects.all()
        return queryset

class DeviceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


