from django.urls import path
from .consumers import ChatConsumer

ws_url_patterns = [
    path('ws/notification/<str:roomcode>/', ChatConsumer.as_asgi()),
]