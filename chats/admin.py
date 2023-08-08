from django.contrib import admin
from chats.models import Community_messages,Friends_chat

# Register your models here.


class Community_MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_time']

class Friends_chatAdmin(admin.ModelAdmin):
    list_display=['user1','user2']
admin.site.register(Community_messages,Community_MessageAdmin)
admin.site.register(Friends_chat,Friends_chatAdmin)
