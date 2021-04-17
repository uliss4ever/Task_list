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
    date_add = models.DateTimeField(default=lambda:datetime.today() + timedelta(days=1))
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    task_types = models.ForeignKey(TaskType, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(max_length=500)
    date_add = models.DateTimeField(default=lambda: datetime.now())
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    task_id=models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments') # TODO поменять имя на task (везде)

    def __str__(self):
        return self.text



