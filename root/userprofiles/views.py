from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
from .forms import user_registeration_form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# ---------- USER REGISTRATION/LOGIN/LOGOUT -------------

def register_view(request) :
    form = user_registeration_form(request.POST)

    context = {
        'form' :form,
    }

    if request.method == 'POST' :
        if form.is_valid() :
            form.save()
            username = request.POST['username']
            user = User.objects.get(username = username)

            return redirect(loginview)

    return render(request, 'register.html', context=context)

def loginview(request) :
    if request.user.is_authenticated :
        return HttpResponse("you are already logged in")

    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None :
            # login into the website
            login(request, user)
            return redirect('main:home')
            # return HttpResponse("you are already logged in")
        else :
            # authentication failed
            messages.error(request, "username or password is incorrect")
            pass
    return render(request, 'login.html', context={})

@login_required(login_url=loginview)
def logoutview(request) : 
    logout(request)
    return redirect(loginview)
