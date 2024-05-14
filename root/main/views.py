from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from userprofiles.models import user_profile
# Create your views here.

def homeview(request) :
    return HttpResponse(f"this is home page , welcome {request.user.username}")

def chatroomview(request, roomcode) :
    chatroom = Chatroom.objects.get(code = roomcode)
    messages_list = messages.objects.filter(chatroom = chatroom)

    context = {
        'chatroom' : chatroom,
        'user' : request.user,
        'messages' : messages_list,
    }

    if request.method == 'POST' :
        content = request.POST['message']
        sender = user_profile.objects.get(user = request.user)

        messages.objects.create(content = content, sender = sender, chatroom = chatroom)

        return redirect(f"/main/chatroom/{roomcode}")

    return render(request, 'chatroom.html', context=context)