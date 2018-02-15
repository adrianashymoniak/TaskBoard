from datetime import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)
    task_title = models.CharField(max_length=150)
    task_description = models.TextField(max_length=250)
    time_estimated = models.DateField(null=True)
    time_published = models.DateTimeField(default=datetime.now, blank=True)
    time_edited = models.DateTimeField(null=True, blank=True)

    def published(self):
        self.time_published = timezone.now()
        self.save()

    def __str__(self):
        return self.task_title, self.task_description

