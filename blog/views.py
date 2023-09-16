from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blog.models import Post


def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def blog_single(request,pid):
    post = get_object_or_404(Post,pk = pid,status=1)
    context = {"post":post}
    return render(request, "blog/blog-single.html",context)


# example for url parameter And error 404 :)
def text(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {"id": post}
    return render(request, "blog/text.html", context)


# template tags in html
def test(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/test.html", context)
