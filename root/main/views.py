from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q

from .models import *
from .forms import *

from userprofiles.models import user_profile
from userprofiles.views import loginview
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib import messages as django_messages

from .matchmaking import get_keywords

# Create your views here.

@login_required(login_url=loginview)
def searchview(request) :
    squery = request.GET['searchquery']
    asked_rooms = Chatroom.objects.filter(Q(desc__contains=squery)|Q(name__contains=squery))
    joined_chatrooms = Chatroom.objects.filter(joinedchatrooms__user=user_profile.objects.get(user=request.user))
    final_joined = []
    for chatroom in joined_chatrooms:
        final_joined.append(chatroom)

    context = {
        'rooms' : asked_rooms,
        'final_joined' : final_joined,
    }
    if request.method == 'POST' :
        s = request.POST['search']
        return redirect(f'/main/searchview/?searchquery={s}')
    return render(request, 'searchview.html', context=context)
    

@login_required(login_url=loginview)
def homeview(request) :
    user_profile_instance = user_profile.objects.get(user=request.user)
    joined_chatrooms = Chatroom.objects.filter(joinedchatrooms__user=user_profile_instance)
    not_joined_chatrooms = Chatroom.objects.exclude(joinedchatrooms__user=user_profile_instance)
    final_joined = []
    final_not_joined = []

    for chatroom in joined_chatrooms:
        final_joined.append(chatroom)

    for chatroom in not_joined_chatrooms:
        final_not_joined.append(chatroom)
    
    if request.method == 'POST' :
        s = request.POST['search']
        return redirect(f'/main/searchview/?searchquery={s}')

    keywords = get_keywords(user_profile_instance.bio)
    keywords = [x.lower() for x in keywords]
    print('===========================================')
    print(user_profile_instance.bio)
    print(keywords)
    suggested_rooms = []
    for room in final_not_joined :
        if len(list(set(keywords) & set(room.desc.split(' ')))) > 0:
            suggested_rooms.append(room)
    print('===========================================')

    try :
        asked_chatroom = request.GET['searchquery']
        chatrooms = Chatroom.objects.filter(name__contains = asked_chatroom)
        return HttpResponse(f"here are the results : ")
    except :
        pass

    all_chatrooms = Chatroom.objects.all()

    context = {
        'user' : user_profile_instance,
        'joined_chatrooms' : set(final_joined),
        'other_chatrooms' : set(final_not_joined),
        'suggested_rooms' : set(suggested_rooms),
    }

    return render(request, 'home.html', context = context)

@login_required(login_url=loginview)
def chatroomview(request, roomcode) :
    user_profile_instance = user_profile.objects.get(user=request.user)
    chatroom = Chatroom.objects.get(code = roomcode)
    messages_list = messages.objects.filter(chatroom = chatroom)
    form = chatmessagecreationform(request.POST)
    joined_chatrooms = Chatroom.objects.filter(joinedchatrooms__user=user_profile_instance)

    context = {
        'chatroom' : chatroom,
        'user' : request.user,
        'messages' : messages_list,
        'form' : form,
        'roomcode' :roomcode,
        'joined_chatrooms' : joined_chatrooms,
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
        pass
    return


@login_required(login_url=loginview)
def chatroom_dashboard(request, username):
    pass

@login_required(login_url=loginview)
def join_chatroom(request, roomcode):
    room = Chatroom.objects.get(code = roomcode)
    user = user_profile.objects.get(user = request.user)
    JoinedChatrooms.objects.create(user = user, chatroom = room)
    return redirect('/main')

@login_required(login_url=loginview)
def leave_chatroom(request, roomcode):
    room = Chatroom.objects.get(code = roomcode)
    user = user_profile.objects.get(user = request.user)
    try :
        chatroom_to_leave = JoinedChatrooms.objects.get(user = user, chatroom = room)
        print(chatroom_to_leave)
        chatroom_to_leave.delete()
        return redirect('/main')
    except :
        return redirect('/main')
    
@login_required(login_url=loginview)
def create_chatroom(request):
    if request.method == 'POST':
        form = ChatroomForm(request.POST)
        if form.is_valid():
            chatroom = form.save(commit=False)
            chatroom.code = generate_random_code()
            chatroom.save()
            django_messages.success(request, 'Chatroom successfully created.')

        else:
            django_messages.error(request, 'This name is already taken.')
    else:
        form = ChatroomForm()
    return render(request, 'create_chatroom.html', {'form': form})


# ---------------------------- brain ------------------------------- :

import random

def generate_random_code(length=7):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string