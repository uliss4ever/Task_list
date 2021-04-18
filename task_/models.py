from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# class TaskType(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name



def fun_time():
    return datetime.today() + timedelta(days=1)

class Task(models.Model):
    ACTIVE_ST = 'A'
    HIDDEN_ST = "H"
    DONE_ST = 'D'
    STATUS_CHOICES = [
        (ACTIVE_ST, 'Активно'),
        (HIDDEN_ST, 'Отложено'),
        (DONE_ST, 'Выполнено'),
    ]


    title = models.CharField(max_length=255)
    public = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    date_add = models.DateTimeField(default=fun_time)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    task_types = models.CharField(max_length=2, choices=STATUS_CHOICES, default=ACTIVE_ST)

    # task_types = models.ForeignKey(TaskType, on_delete=models.PROTECT, default=1)



    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(max_length=500)
    date_add = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    task_id=models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments') # TODO поменять имя на task (везде)

    def __str__(self):
        return self.text



