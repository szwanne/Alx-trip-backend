from django.shortcuts import render
from .serializers import UserProfileSerializer
from trip.models import UserProfile
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.

class UserProfileList(generics.ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.all()
