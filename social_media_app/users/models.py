from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, default='media/profilepic.jpg')
    
    def __str__(self):
        return self.user.username