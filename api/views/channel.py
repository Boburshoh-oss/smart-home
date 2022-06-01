from rest_framework import viewsets
from api.serializers import ChannelSerializer
from core.models import Channel


class ChannelViewSet(viewsets.ModelViewSet):
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()
