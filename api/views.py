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
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.db import IntegrityError


from rest_framework import generics, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .serializers import (
    UserProfileSerializer,
    ActivitySerializer,
    TripSerializer,
    DestinationSerializer,
    TripMemberSerializer,
    BookingSerializer,
    FlightOfferSerializer,
    HotelSerializer,
    WeatherSerializer,
    ItinerarySerializer,
    ItineraryItemSerializer,
    RegisterSerializer
)
from trip.models import (
    UserProfile,
    Activity,
    Trip,
    Destination,
    TripMember,
    Booking,
    FlightOffer,
    Hotel,
    Weather,
    Itinerary,
    ItineraryItem
)


# # -------------------------------
# # Authentication Views
# # -------------------------------

@api_view(['POST', 'PUT'])
@permission_classes([AllowAny])  # anyone can sign up
def signup(request):
    """
    Create a new user account
    """
    data = request.data
    try:
        user = User.objects.create_user(
            username=data['username'],
            password=data['password']
        )
        user.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    except IntegrityError:
        return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

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
# FlightOffer Views
# -------------------------------

class FlightOfferListCreate(generics.ListCreateAPIView):
    """
    List all avail flight offers or can create a new one.
    Requires authentication.
    """
    serializer_class = FlightOfferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FlightOffer.objects.all()


class FlightOfferRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a flightoffer by ID.
    Requires authentication.
    """

    serializer_class = FlightOfferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Restrict access to the logged-in user’s flightOffer
        return FlightOffer.objects.filter(user=self.request.user)


# -------------------------------
# Hotel Views
# -------------------------------

class HotelListCreate(generics.ListCreateAPIView):
    """
    List all destinations or create a new one.
    Requires authentication.
    """
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Hotel.objects.all()


class HotelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a flightoffer by ID.
    Requires authentication.
    """

    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Restrict access to the logged-in user’s flightOffer
        return Hotel.objects.filter(user=self.request.user)


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


class DestinationActivitiesList(generics.ListAPIView):
    """
    List all activities for a given destination (by destination ID).
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ActivitySerializer

    def get_queryset(self):
        dest_id = self.kwargs.get("pk")
        try:
            destination = Destination.objects.get(pk=dest_id)
        except Destination.DoesNotExist:
            raise NotFound({"error": "Destination not found"})
        return Activity.objects.filter(destination=destination).order_by("-date")


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
        return Trip.objects.filter(user=self.request.user).order_by('-start_date')

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
        return Trip.objects.filter(user=self.request.user).order_by('-start_date')


# -------------------------------
# Weather Views
# -------------------------------

class WeatherListCreate(generics.ListCreateAPIView):
    """
    List all weather or create a new one.
    Requires authentication.
    """
    serializer_class = WeatherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Weather.objects.all()


class WeatherRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a trip by ID.
    Only available for the authenticated user’s own trips.
    """
    serializer_class = WeatherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Restrict access to the logged-in user’s weather
        return Weather.objects.all()


# -------------------------------
# Itinerary Views
# -------------------------------

class ItineraryListCreate(generics.ListCreateAPIView):
    """
    List all weather or create a new one.
    Requires authentication.
    """
    serializer_class = ItinerarySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Itinerary.objects.all()


class ItineraryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a trip by ID.
    Only available for the authenticated user’s own trips.
    """
    serializer_class = ItinerarySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Restrict access to the logged-in user’s weather
        return Itinerary.objects.all()


# -------------------------------
# ItineraryItem Views
# -------------------------------

class ItineraryItemListCreate(generics.ListCreateAPIView):
    """
    List all weather or create a new one.
    Requires authentication.
    """
    serializer_class = ItineraryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ItineraryItem.objects.all()


class ItineraryItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a trip by ID.
    Only available for the authenticated user’s own trips.
    """
    serializer_class = ItineraryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Restrict access to the logged-in user’s weather
        return ItineraryItem.objects.all()
