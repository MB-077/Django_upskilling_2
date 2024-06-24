from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile.jpg', upload_to='profile_pictures')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'