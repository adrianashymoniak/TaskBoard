from datetime import datetime

from django.db import models


# Create your models here.

class Task(models.Model):
    task_title = models.CharField(max_length=150, blank=True)
    task_description = models.CharField(max_length=250, blank=True)
    time_estimated = models.DateTimeField(default=datetime.now, blank=True)
    time_published = models.DateTimeField(default=datetime.now, blank=True)
    time_edited = models.DateTimeField(default=datetime.now, blank=True)
