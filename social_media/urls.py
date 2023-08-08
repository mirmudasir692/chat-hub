from django.contrib import admin
from django.urls import path,include
from chats.views import chat_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',chat_home,name="chat_home"),
    path('accounts/',include(('accounts.urls','accounts'))),
    path('chats/',include(('chats.urls','chats')))
]
