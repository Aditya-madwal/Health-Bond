import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from main import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": application,
    "websocket": URLRouter(
        routing.ws_url_patterns
    ),
})