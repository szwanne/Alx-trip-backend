from django.shortcuts import render
from .serializers import UserProfileSerializer
from trip.models import UserProfile
from rest_framework import generics, permissions
from rest_framework.response import Response


# Create your views here.

class UserProfileListCreate(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.all()


class UserProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Only users can only update, delete their profile
        return UserProfile.objects.all()
