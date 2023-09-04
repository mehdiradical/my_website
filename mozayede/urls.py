from django.contrib import admin
from django.urls import path
from mozayede.views import *

urlpatterns = [
    path("", home),
    path("contact/", contact),
    path("about/", about),
]
