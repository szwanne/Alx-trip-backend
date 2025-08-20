from django.shortcuts import render
from .serializers import UserProfileSerializer, ActivitySerializer, TripSerializer, DestinationSerializer, TripMemberSerializer, BookingSerializer
from trip.models import UserProfile, Activity, Trip, Destination, TripMember, Booking
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

# Create your views here.


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)  # Parse JSON body
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            user.save()
            token = Token.objects.create(user=user)
            # make sure this is indented correctly
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse(
                {'error': 'username taken. choose another username'},
                status=400
            )
    else:
        # fallback response
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request,
            username=data['username'],
            password=data['password']
        )

        if user is None:
            return JsonResponse(
                {'error': 'Unable to login. Check username and password'},
                status=400
            )
        else:
            # return user token
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:  # cleaner than bare except
                token = Token.objects.create(user=user)

            return JsonResponse({'token': str(token)}, status=201)

    # fallback if request method is not POST
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


class BookingListCreate(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.all()


class BookingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.all()


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


class TripMemberRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
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
