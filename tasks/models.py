from datetime import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)
    task_title = models.CharField(max_length=150, blank=True)
    task_description = models.CharField(max_length=250, blank=True)
    time_estimated = models.DateTimeField(default=datetime.now, blank=True)
    time_published = models.DateTimeField(default=datetime.now, blank=True)
    time_edited = models.DateTimeField(default=datetime.now, blank=True)

    def published(self):
        self.time_published = timezone.now()
        self.save()

    def __str__(self):
        return self.task_title
