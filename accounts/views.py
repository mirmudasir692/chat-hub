from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from accounts.models import CustomUser, BlockList
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.


def Login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            user_check = blocked_user_check(request, user)
            if user_check:
                login(request, user)
                return redirect('chats:chat_home')
            else:
                messages.error(request, 'You are blocked')
                return redirect('accounts:login_user')
        else:
            messages.warning(request, "Please enter the right credentials")
            return redirect('accounts:login_user')
    return render(request, 'accounts/login.html')


def blocked_user_check(request, user):
    blocked_users = BlockList.objects.all()
    for blocked_user in blocked_users:
        if blocked_user.user == user:
            return False
    return True


def create_user(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            username = request.POST.get('username')
            email = request.POST.get('email')
            age = request.POST.get('age')
            birthday = request.POST.get('birthday')
            user = authenticate(username=username, password=password2)
            if user is None:
                user = CustomUser.objects.create_user(
                    username=username, email=email, password=password2, birthday=birthday)
                login(request, user)
                return redirect('chats:chat_home')
            else:
                messages.error(request, 'user already registered')
                return redirect('accounts:create_user')

        else:
            messages.error(request, 'Passwords should be same')
            return redirect("accounts/login")

    return render(request, 'accounts/create.html')


def logout_user(request):
    logout(request)
    return redirect("accounts:login_user")


def user_profile(request):
    user = CustomUser.objects.get(username=request.user)
    print(user.birthday)
    content = {'user': user}
    return render(request, 'accounts/profile.html', content)


def delete_user(request):
    user = request.user
    User = get_object_or_404(CustomUser, username=user)
    if User.delete():
        return redirect("chats:chat_home")
    return redirect('chats:chat_home')


def friend_profile(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    content = {'user': user}
    return render(request, 'accounts/friend_info.html', content)
