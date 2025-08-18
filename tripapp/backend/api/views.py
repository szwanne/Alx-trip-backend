from django.shortcuts import render
from .serializers import UserProfileSerializer, ActivitySerializer, TripSerializer, DestinationSerializer, TripMemberSerializer
from trip.models import UserProfile, Activity, Trip, Destination, TripMember
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


class ActivityListCreate(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.all()


class ActivityRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.all()


class DestinationListCreate(generics.ListCreateAPIView):
    serializer_class = DestinationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Destination.objects.all()


class DestinationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DestinationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Destination.objects.all()


class TripMemberListCreate(generics.ListCreateAPIView):
    serializer_class = TripMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TripMember.objects.all()


class TripListCreate(generics.ListCreateAPIView):
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class TripRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)
