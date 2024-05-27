import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import *
from userprofiles.models import user_profile
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['roomcode']}"
        print(self.room_name)
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        print('+++++++++++++++++++++++')
        print(type(text_data))
        text_data_json = json.loads(text_data)
        print(type(text_data_json))
        print('+++++++++++++++++++++++')

        # msg = text_data_json
        event = {
            'type' : 'send_message',
            'message' : text_data_json,
        }

        await self.channel_layer.group_send(self.room_name, event)

    # this send_message method sends the message recieved to everyone in the group and also calls the create_message method to manpulate database in the background

    async def send_message(self, event):
        data = event['message']
        print('----------------------------')
        print(data)
        print('----------------------------')
        await self.create_message(data=data)
        response_data = {
            'sender': data['sender_username'],
            'message': data['message'],
            'roomcode' : data['room_code'],
        }
        await self.send(text_data=json.dumps({'message': response_data}))
    
    # note : we cant perform database manipulations in async functions thus we create a seperate sync_to_async database method :
    @database_sync_to_async
    def create_message(self, data):
        print('[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]')
        data_dict = json.dumps(data)
        data_dict = json.loads(data_dict)
        print(data_dict)
        print(type(data_dict))
        message = data_dict.get("message")
        sender = user_profile.objects.get(user = User.objects.get(username = data_dict.get('sender_username')))
        room = Chatroom.objects.get(code = data_dict.get('room_code'))

        if not messages.objects.filter(content=data['message']).exists():
            messages.objects.create(content = message, chatroom = room, sender = sender).save()
