from rest_framework import routers
from django.urls import path, include

from api.views import UserViewSet, RoomViewSet, HomeViewSet, ChannelViewSet, DeviceViewSet, ProductViewSet, SensorViewSet

router = routers.DefaultRouter()

router.register('auth', UserViewSet)
router.register('room', RoomViewSet)
router.register('home', HomeViewSet)
router.register('channel', ChannelViewSet)
router.register('device', DeviceViewSet)
router.register('product', ProductViewSet)
router.register('sensor', SensorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
