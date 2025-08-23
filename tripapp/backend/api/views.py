"""
views.py - API Views for Trip Planner Application

This file contains API endpoints for:
- Authentication (signup & login) using `rest_framework.authtoken`
- CRUD operations for:
  - Booking
  - UserProfile
  - Activity
  - Destination
  - TripMember
  - Trip

We use Django REST Framework's generic views for common CRUD functionality
and custom views for authentication.
"""

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


from rest_framework import generics, permissions
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import (
    UserProfileSerializer,
    ActivitySerializer,
    TripSerializer,
    DestinationSerializer,
    TripMemberSerializer,
    BookingSerializer
)
from trip.models import (
    UserProfile,
    Activity,
    Trip,
    Destination,
    TripMember,
    Booking
)


# -------------------------------
# Authentication Views
# -------------------------------

@csrf_exempt
def signup(request):
    """
    User signup endpoint.
    Method: POST
    Body: { "username": "<username>", "password": "<password>" }
    Returns: JSON { "token": "<auth_token>" }

    Creates a new user and generates an authentication token.
    """
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)  # Parse JSON body
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            user.save()

            # Generate token for new user
            token = Token.objects.create(user=user)

            return JsonResponse({'token': str(token)}, status=201)

        except IntegrityError:
            return JsonResponse(
                {'error': 'Username already taken. Choose another one.'},
                status=400
            )

    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


@csrf_exempt
def login(request):
    """
    User login endpoint.
    Method: POST
    Body: { "username": "<username>", "password": "<password>" }
    Returns: JSON { "token": "<auth_token>" }

    Authenticates a user and returns their token.
    If token does not exist, creates a new one.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request,
            username=data['username'],
            password=data['password']
        )

        if user is None:
            return JsonResponse(
                {'error': 'Unable to login. Check username and password.'},
                status=400
            )

        # Fetch or create token
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': str(token)}, status=200)

    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


# -------------------------------
# Booking Views
# -------------------------------

class BookingListCreate(generics.ListCreateAPIView):
    """
    List all bookings or create a new booking.
    Requires authentication.
    """
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.all()


class BookingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a booking by ID.
    Requires authentication.
    """
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.all()


# -------------------------------
# UserProfile Views
# -------------------------------

class UserProfileListCreate(generics.ListCreateAPIView):
    """
    List all user profiles or create a new one.
    Requires authentication.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.all()


class UserProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a user profile by ID.
    Requires authentication.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.all()


# -------------------------------
# Activity Views
# -------------------------------

class ActivityListCreate(generics.ListCreateAPIView):
    """
    List all activities or create a new activity.
    Requires authentication.
    """
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.all()


class ActivityRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete an activity by ID.
    Requires authentication.
    """
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.all()


# -------------------------------
# Destination Views
# -------------------------------

class DestinationListCreate(generics.ListCreateAPIView):
    """
    List all destinations or create a new one.
    Requires authentication.
    """
    serializer_class = DestinationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Destination.objects.all()


class DestinationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a destination by ID.
    Requires authentication.
    """
    serializer_class = DestinationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Destination.objects.all()


# -------------------------------
# TripMember Views
# -------------------------------

class TripMemberListCreate(generics.ListCreateAPIView):
    """
    List all trip members or create a new member.
    Requires authentication.
    """
    serializer_class = TripMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TripMember.objects.all()


class TripMemberRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a trip member by ID.
    Requires authentication.
    """
    serializer_class = TripMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TripMember.objects.all()


# -------------------------------
# Trip Views
# -------------------------------

class TripListCreate(generics.ListCreateAPIView):
    """
    List all trips for the authenticated user or create a new trip.
    Requires authentication.
    """
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return trips belonging to the logged-in user
        return Trip.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Ensure the trip is linked to the logged-in user
        return serializer.save(user=self.request.user)


class TripRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a trip by ID.
    Only available for the authenticated user’s own trips.
    """
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Restrict access to the logged-in user’s trips
        return Trip.objects.filter(user=self.request.user)
