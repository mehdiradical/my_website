


from django.http import HttpResponse
from django.http import JsonResponse

def pasokh(request):
    
    return HttpResponse("<h1> This is my first Professioanal webSite </h1>")

def pasokh_json(request):
    return JsonResponse({"name":"mahdi"})