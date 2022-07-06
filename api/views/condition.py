from rest_framework import generics
from core.models import Condition
from api.serializers import SmartConditionSerializer
from core.models.condition import SmartCondition

class SmartConditionListCreateApiView(generics.ListCreateAPIView):
    serializer_class = SmartConditionSerializer
    queryset = SmartCondition.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)

class SmartConditionRetrieveApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SmartConditionSerializer
    queryset = SmartCondition.objects.all()