from django.db import models
from accounts.models import CustomUser

# Create your models here.


class Community_messages(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)
    date_time = models.DateTimeField(auto_now_add=True)
    timespan = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        message_words = self.message.split()[:100]
        truncated_message = " ".join(message_words)
        return f"{truncated_message} by {self.user}"


class Friends_chat(models.Model):
    message = models.TextField(max_length=1000)
    user1 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='sender')
    user2 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='receiver')
    date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"message for {self.user2} by {self.user1}"
