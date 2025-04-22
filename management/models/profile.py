
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='media/profile_pics/', null=True, blank=True)
    name = models.CharField(max_length=255)
    join_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
