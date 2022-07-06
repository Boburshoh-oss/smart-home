from rest_framework import viewsets

from api.serializers import ProductSerializer
from core.models.product import Product


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
