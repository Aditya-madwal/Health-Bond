from django.db import models
from userprofiles.models import user_profile
import datetime
# Create your models here.

class Chatroom(models.Model) :
    code =  models.CharField(max_length=7)
    name = models.CharField(max_length=20, unique=True)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}({self.code})"

class messages(models.Model) :
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(max_length=1000)
    sender = models.ForeignKey(user_profile, on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=0)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class JoinedChatrooms(models.Model) :
    user = models.ForeignKey(user_profile,on_delete=models.CASCADE)
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.chatroom} --> {self.user.user.username}"
    
