from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class user_registeration_form(UserCreationForm) :
    class Meta :
        model = User
        fields = ['username','first_name','last_name' ,'email', 'password1', 'password2']

