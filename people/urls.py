from django.contrib import admin
from django.urls import path, include
from people.views import register

urlpatterns = [
    path('register/', register, name="register"),
]
