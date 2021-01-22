from django.conf import settings
from django.db import models
from django.utils import timezone

class Todo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #작성자
    title = models.CharField(max_length=20) #할 일
    deadline = models.DateTimeField(blank=True, null=True) #마감일

def __str__(self):
    return self.title
