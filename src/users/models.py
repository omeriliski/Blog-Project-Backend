from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.TextField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

