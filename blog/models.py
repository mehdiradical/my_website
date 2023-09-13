from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(null=True)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)
