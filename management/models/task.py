from django.db import models
from django.contrib.auth.models import User
from .project import Project

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(
        User, on_delete=models.PROTECT,
        related_name='tasks'
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        related_name='tasks'
    )
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title