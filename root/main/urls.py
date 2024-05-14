from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'

# urls.py
urlpatterns = [
    path('', views.homeview, name='home'),
    path('chatroom/<slug:roomcode>',views.chatroomview, name = 'chatroom'),
]