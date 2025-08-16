from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username
