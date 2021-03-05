from django.conf import settings
from django.db import models


# Create your models here.

class Chat(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='receiver', on_delete=models.CASCADE)
    text = models.CharField(max_length=225, verbose_name='chat', default='write message...',)
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'message from {self.sender} to {self.recipient}'
