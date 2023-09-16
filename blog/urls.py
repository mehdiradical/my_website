from django.urls import path
from blog.views import *

app_name = "blog"
urlpatterns = [
    path("", blog_view, name="bindex"),
    path("<int:pid>", blog_single, name="blogsingle"),
    path("test", test, name="test"),
    path("post-<int:pid>", text, name="texttttt"),
]
