from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    type = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.type

class InterestCircle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='created_circles', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
