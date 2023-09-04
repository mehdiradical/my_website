from django.contrib import admin
from django.urls import path
from mozayede.views import home_view, about_view, contact_view

urlpatterns = [
    path("", home_view),

]
