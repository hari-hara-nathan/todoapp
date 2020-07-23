from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    author = models.CharField(max_length=30,name='author')
    todo_item = models.TextField(max_length=45)
    lastdate = models.DateField(default=timezone.now)
    done = models.BooleanField(default=False)
    objects = models.manager

    def __str__(self):
        return self.username
