from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.serializers import HomeSerializer
from core.models.home import Home

class HomeListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = HomeSerializer
    queryset = Home.objects.all()
            
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = Home.objects.filter(owner=user)
        else:
            queryset = Home.objects.all()
        return queryset

class HomeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = HomeSerializer
    queryset = Home.objects.all()
            
    
# class HomeViewSet(viewsets.ModelViewSet):
#     serializer_class = HomeSerializer
#     queryset = Home.objects.all()
    
#     def perform_crea(self, serializer):
#         serializer.save(owner=self.request.user)