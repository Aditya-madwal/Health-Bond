from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import chatmessagecreationform

from userprofiles.models import user_profile
from userprofiles.views import loginview
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url=loginview)
def homeview(request) : 
    user = user_profile.objects.get(user = request.user)
    joined_chatrooms = JoinedChatrooms.objects.filter(user = user)
    all_chatrooms = Chatroom.objects.all()
    final_not_joined = []

    for i in all_chatrooms :
        for j in joined_chatrooms :
            if i == j.chatroom :
                pass
            else :
                final_not_joined.append(i)

    if request.GET['searchquery'] :
        asked_chatroom = request.GET['searchquery']
        chatrooms = Chatroom.objects.filter(name = asked_chatroom)
        return HttpResponse(f"{str(chatrooms)}")

    all_chatrooms = Chatroom.objects.all()

    context = {
        'user' : user,
        'joined_chatrooms' : joined_chatrooms,
        'other_chatrooms' : final_not_joined,
    }

    return render(request, 'home.html', context = context)

@login_required(login_url=loginview)
def chatroomview(request, roomcode) :
    chatroom = Chatroom.objects.get(code = roomcode)
    messages_list = messages.objects.filter(chatroom = chatroom)
    form = chatmessagecreationform(request.POST)

    context = {
        'chatroom' : chatroom,
        'user' : request.user,
        'messages' : messages_list,
        'form' : form,
        'roomcode' :roomcode,
    }

    if request.method == 'POST' :
        if form.is_valid() :
            message = form.save(commit = False)
            sender = user_profile.objects.get(user = request.user)
            message.sender = sender
            message.chatroom = chatroom
            message.save()
            return redirect(f'/main/chatroom/{roomcode}')

    return render(request, 'chatroom.html', context=context)

@login_required(login_url=loginview)
def user_dashboard(request, username):
    if username == request.user.username :
        # account holder is viewing his own dashboard :
        pass
    else :
        # user is viewing someone else's dashboard :


@login_required(login_url=loginview)
def chatroom_dashboard(request, username):
    pass
