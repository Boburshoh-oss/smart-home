"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
import os
import django

django.setup()

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ChannelNameRouter, ProtocolTypeRouter, URLRouter
from api.consumers import websocket_urlpatterns
from chanmqttproxy import MqttConsumer
from api.jwt_middleware.auth import JWTAuthMiddlewareStack

application = ProtocolTypeRouter(
    {
        "channel": ChannelNameRouter({"mqtt": MqttConsumer.as_asgi()}),
        "http": get_asgi_application(),
        "websocket": JWTAuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
    }
)
