from django.db import models
from django.contrib.auth.models import User
from circles.models import InterestCircle

class Chat(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    circle = models.ForeignKey(InterestCircle, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} - {self.timestamp}'