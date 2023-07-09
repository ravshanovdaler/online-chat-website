from django.db import models
from django.conf import settings

class Messages(models.Model):
    text = models.TextField()
    message_author = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(auto_now_add=True)

class MessagesToAdmin(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()