from django.contrib import admin
from mozayede.models import Contact
# Register your models here.

@admin.register(Contact)
#admin.site.register(Contact,ContactAdmin)

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email',"message",'created_date')
    list_filter = ('email',)
    search_fields = ('name','message')

