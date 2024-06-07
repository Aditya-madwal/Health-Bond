from django import forms
from django.forms import ModelForm

from .models import *
from userprofiles.models import *

class chatmessagecreationform(forms.ModelForm):
    class Meta:
        model = messages
        fields = ['content']

class ChatroomForm(forms.ModelForm):
    class Meta:
        model = Chatroom
        fields = ['name', 'desc']

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = ['pfp']
