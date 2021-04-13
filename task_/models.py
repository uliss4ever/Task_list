from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    public = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    date_add = models.DateTimeField(default=datetime.today() + timedelta(days=1))
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    task_types = models.ForeignKey(TaskType, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.title

class Comments(models.Model):
    text = models.TextField(max_length=500)
    public = models.BooleanField(default=False) # для публичных заметок (??)
    date_add = models.DateTimeField(default=datetime.today())
    # user = models.ForeignKey(User, on_delete=models.PROTECT())

    def __str__(self):
        return self.text