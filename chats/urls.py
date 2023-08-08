from django.urls import path
from .import views
urlpatterns = [
    path('', views.chat_home, name="chat_home"),
    path('community', views.community_chat, name='community'),
    path('Direct_messages', views.Direct_message, name="Direct_messages"),
    path('community_delete/<int:message_id>/',
         views.community_delete, name="community_delete"),
    path('DM_friend/<int:user_id>/', views.Direct_message_send, name="DM_friend"),
    path('DM_delete/<int:message_id>/', views.DM_delete, name="DM_delete"),
]
