from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username


class Activity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name='activities')

    def __str__(self):
        return self.name


class TripMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=500, unique=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Trip(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trips")
    trip_member = models.ForeignKey(
        TripMember, on_delete=models.CASCADE, related_name="tripmembers")
    title = models.CharField(max_length=100)
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name='trips')
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - ({self.destination.name})"
