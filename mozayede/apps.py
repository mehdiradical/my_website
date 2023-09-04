from django.apps import AppConfig
from django.http import HttpResponse


class MozayedeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mozayede"


def home_view(request):
    return HttpResponse("<h1>Hi This is 'mozayede' Homa Page</h1>")


def about_view(request):
    return HttpResponse("<h1>About us</h1>")

def contact_view(request):
    return HttpResponse("<h1>Contact us</h1>")
