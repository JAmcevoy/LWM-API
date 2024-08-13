from django.db import models
from django.contrib.auth.models import User
from circles.models import Category
from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size_kb = 10240 
    if file.size > max_size_kb * 1024:
        raise ValidationError(f"File size exceeds {max_size_kb} KB limit.")

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    steps = models.TextField(blank=True)
    image_or_video = models.FileField(
        upload_to='posts/media/', 
        validators=[validate_file_size], 
        blank=True, 
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    

    def __str__(self):
        return self.title

