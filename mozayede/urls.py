from django.contrib import admin
from django.urls import path
from mozayede.views import *

app_name = "mozayede"
urlpatterns = [
    path("", home,name='index'),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    
]
