from django.dispatch import Signal,receiver
from chats.models import Friends_chat
from django.db.models.signals import post_save


@receiver(post_save,sender=Friends_chat)
def send_notification(sender,instance,created,**kwargs):
    if created:
        sender=instance.user1
        recipient=instance.user2

