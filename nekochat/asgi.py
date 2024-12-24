import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import room.routing 
import room.consumers
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nekochat.settings')

#websocket_urlpatterns = [
#    path('ws/', room.consumers.ChatConsumer.as_asgi())
#]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            room.routing.websocket_urlpatterns
        )
    )
    #"websocket": URLRouter(websocket_urlpatterns),
})
