from rest_framework import routers
from django.urls import path, include

from api.views import (ChannelListCreateAPIView, ChannelDetailAPIView,
                        SmartConditionListCreateApiView,SmartConditionRetrieveApiView,
                       ProductViewSet, HomeListCreateAPIView, UserRegisterView,UserDetailUpdateView,DescriptionListCreateApiView, HomeDetailAPIView)
from api.views.device import DeviceDetailAPIView, DeviceListCreateAPIView
from api.views.sensor import SensorDetailAPIView, SensorListCreateAPIView


router = routers.DefaultRouter()

# router.register('auth', UserViewSet)
# router.register('home', HomeViewSet)
# router.register('channel', ChannelViewSet)
# router.register('device', DeviceViewSet)
router.register('product', ProductViewSet)
# router.register('sensor', SensorViewSet)
# router.register('register', UserRegisterView)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', HomeListCreateAPIView.as_view()),
    path('home/<int:pk>/', HomeDetailAPIView.as_view()),
    path('channel/', ChannelListCreateAPIView.as_view()),
    path('channel/<int:pk>/', ChannelDetailAPIView.as_view()),
    path('device/', DeviceListCreateAPIView.as_view()),
    path('device/<int:pk>/', DeviceDetailAPIView.as_view()),
    path('sensor/', SensorListCreateAPIView.as_view()),
    path('sensor/<int:pk>/', SensorDetailAPIView.as_view()),
    path('smartconditions/', SmartConditionListCreateApiView.as_view()),
    path('smartconditions/<int:pk>/', SmartConditionRetrieveApiView.as_view()),
    # path('product/', ProductViewSet.as_view()),
    path('register/', UserRegisterView.as_view()),
    path('me/<int:pk>/', UserDetailUpdateView.as_view()),
    path('description/',DescriptionListCreateApiView.as_view())
]
