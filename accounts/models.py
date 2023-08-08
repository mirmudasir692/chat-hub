from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from datetime import date

# Create your models here.


class CustomUser_Manager(BaseUserManager):
    def create_user(self, username, password, email, **kwargs):
        if not username or not email:
            raise ValueError("Email and Password both are required")
        username = self.normalize_email(username)
        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self.create_user(username, password, email, **kwargs)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True, default=None)
    create_on = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username

    objects = CustomUser_Manager()


class extra_user_info(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    browser = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"info of {self.user.username}"


class BlockList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
