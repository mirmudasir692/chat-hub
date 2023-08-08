from django.urls import path
from . import views

urlpatterns=[
    path('',views.Login_user,name="login_user"),
    path('create_user',views.create_user,name="create_user"),
    path('delete_user',views.delete_user,name="delete_user"),
    path('logout_user',views.logout_user,name="logout_user"),
    path('user_profile',views.user_profile,name="user_profile"),
    path('friend_info/<int:user_id>/',views.friend_profile,name="friend_info")
]