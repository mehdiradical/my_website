from django.contrib import admin
from blog.models import Post
# Register your models here.


@admin.register(Post)
# Or
# admin.site.register(Post,PostAdmin)

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ("title","counted_view","status","published_date","updated_date","author",)
    list_filter = ("status","published_date","author",)
    #ordering = ("-created_date",)
    search_fields = ["title","published_date",]