from django.contrib import admin
from django.urls import path,include

from .views import my_view

urlpatterns = [
    path('home', my_view),
]