from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Community_messages, Friends_chat
import json
from django.contrib import messages
from accounts.models import CustomUser
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from accounts.views import blocked_user_check
from django.contrib.auth import logout

# Create your views here.


def chat_home(request):
    user = request.user
    user_check = blocked_user_check(request, user)

    if not user_check:
        logout(request)
        return redirect('chats:chat_home')
    return render(request, 'chats/index.html')


def community_chat(request):
    if request.method == 'POST':
        user_data = json.loads(request.body)
        user_message = user_data['message']
        user_message_string = user_message.lower().split()
        if not 'ashwin' in user_message_string and 'Ashwin' not in user_message_string:
            Community_messages.objects.create(
                user=request.user, message=user_message)
        else:
            return HttpResponse("you can't send it or you will be banned")
    messages = Community_messages.objects.all()
    content = {'messages': messages}
    return render(request, 'chats/community.html', content)


def Direct_message(request):
    users = CustomUser.objects.exclude(username=request.user.username)
    content = {'users': users}
    return render(request, 'chats/DM.html', content)


@never_cache
def Direct_message_send(request, user_id):
    user2 = get_object_or_404(CustomUser, id=user_id)
    if request.method == "POST":
        message = request.POST.get('message')
        user2 = get_object_or_404(CustomUser, id=user_id)
        Friends_chat.objects.create(
            user1=request.user, user2=user2, message=message)
        return redirect('chats:DM_friend', user_id)
    friend = get_object_or_404(CustomUser, id=user_id)
    chats = Friends_chat.objects.filter(
        user1=request.user, user2=friend) | Friends_chat.objects.filter(user1=friend, user2=request.user)
    chats = chats.order_by('date_time')
    content = {'messages': chats, 'user': friend}
    return render(request, 'chats/DM_friend.html', content)


def DM_delete(request, message_id):
    try:
        message = Friends_chat.objects.get(id=message_id)
        if message.user1 == request.user:
            message.delete()
    except Friends_chat.DoesNotExist:
        print("message not found")
    except Exception as e:
        print(f"error : {e}")

    return redirect(request.META.get('HTTP_REFERER', '/'))


def community_delete(request, message_id):
    try:
        message = Community_messages.objects.get(
            id=message_id, user=request.user)
        message.delete()
    except Community_messages.DoesNotExist:
        print("message not found")
    except Exception as e:
        print(f"error : {e}")
    return redirect(request.META.get('HTTP_REFERER', '/'))
