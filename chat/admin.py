from django.contrib import admin
from .models import Room, Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'date', 'value')
    list_display_links = ('room', 'user', 'date', 'value')
    list_filter = ('room', 'user', 'date')
    ordering =  ('room', 'user', 'date', 'value')
admin.site.register(Message, MessageAdmin)

admin.site.register(Room)