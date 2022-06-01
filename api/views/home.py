from rest_framework import viewsets

from api.serializers import HomeSerializer
from core.models import Home


class HomeViewSet(viewsets.ModelViewSet):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()
