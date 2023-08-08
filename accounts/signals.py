from django.dispatch import Signal, receiver
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from accounts.models import BlockList, CustomUser
from chats.models import Friends_chat, Community_messages
from chats.models import Friends_chat, Community_messages


@receiver(post_save, sender=BlockList)
def delete_messages_of_user(sender, instance, created, **kwargs):
    if created:
        blocked_user = instance.user
        Community_messages.objects.filter(user=blocked_user).delete()
        Friends_chat.objects.filter(user1=blocked_user).delete()
        