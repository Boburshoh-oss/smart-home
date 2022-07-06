from asyncio.log import logger
from rest_framework import generics
from api.serializers import ChannelSerializer
from core.models.channel import Channel
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ChannelListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()
            
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = Channel.objects.filter(owner=user)
        else:
            queryset = Channel.objects.all()
        return queryset
    
    

class ChannelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()


