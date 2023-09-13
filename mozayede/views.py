from django.shortcuts import render


def home(request):
    return render(request, "index.html")

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,"about.html")

def test_view(request):
    return render(request,"test.html",{"name":"mahdi","lname":"saberi"})  

