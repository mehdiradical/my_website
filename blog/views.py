from django.shortcuts import render


def blog_view(request):
    return render(request, "blog/blog-home.html")


def blog_single(request):
    contex = {"title":"Programmer Mr Mahdi Saberizadeh","content":"mahdi saberi zadeh is amazing Programmer!"}
    return render(request, "blog/blog-single.html",contex)
