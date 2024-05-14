from django.contrib import admin
from django.urls import path
from . import views

# urls.py
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
]