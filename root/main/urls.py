from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'

# urls.py
urlpatterns = [
    path('', views.homeview, name='home'),
    path('chatroom/<slug:roomcode>',views.chatroomview, name = 'chatroom'),
    path('joinchatroom/<slug:roomcode>', views.join_chatroom, name = 'joinchatroom'),
    path('leavechatroom/<slug:roomcode>', views.leave_chatroom, name = 'leavechatroom'),
    path('createchatroom/', views.create_chatroom, name = 'createchatroom'),
    path('searchview/', views.searchview, name = 'search'),
    path('user/<slug:username>', views.user_dashboard, name = 'userdashboard'),
    path('view_chatroom/<slug:roomcode>', views.chatroom_dashboard, name = 'chatroomdashboard'),
]