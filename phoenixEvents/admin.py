from django.contrib import admin
from phoenixEvents.models import Event
# Register your models here.
admin.site.register(Event)

#class ArticleAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug': ('eventName', 'eventDate',), }

class AuthorAdmin(admin.ModelAdmin):
    exclude = ('slug',)
