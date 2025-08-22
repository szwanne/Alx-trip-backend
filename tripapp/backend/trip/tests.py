from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Booking, UserProfile, Activity, Destination, TripMember, Trip


class BookingModelTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            type="Hotel",
            detail="5-star luxury hotel",
            booking_date=timezone.now()
        )
        self.assertEqual(str(booking.type), "Hotel")


class UserProfileModelTest(TestCase):
    def test_create_user_profile(self):
        user = User.objects.create_user(username="testuser", password="12345")
        booking = Booking.objects.create(
            type="Flight",
            detail="One-way ticket",
            booking_date=timezone.now()
        )
        profile = UserProfile.objects.create(user=user, booking=booking)
        self.assertEqual(str(profile), "testuser")


class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(
            name="Hiking",
            description="Mountain hike",
            date=timezone.now()
        )
        self.assertEqual(str(activity), "Hiking")


class DestinationModelTest(TestCase):
    def test_create_destination(self):
        activity = Activity.objects.create(
            name="Surfing",
            description="Beach surfing",
            date=timezone.now()
        )
        destination = Destination.objects.create(
            name="Cape Town",
            country="South Africa",
            description="Beautiful beaches",
            activity=activity
        )
        self.assertEqual(str(destination), "Cape Town")


class TripMemberModelTest(TestCase):
    def test_create_trip_member(self):
        member = TripMember.objects.create(
            name="Alice", email="alice@example.com"
        )
        self.assertEqual(str(member), "Alice - alice@example.com")


class TripModelTest(TestCase):
    def test_create_trip(self):
        user = User.objects.create_user(username="john", password="12345")
        member = TripMember.objects.create(name="Bob", email="bob@example.com")
        activity = Activity.objects.create(
            name="Safari",
            description="Wildlife tour",
            date=timezone.now()
        )
        destination = Destination.objects.create(
            name="Kruger Park",
            country="South Africa",
            description="National Park",
            activity=activity
        )
        trip = Trip.objects.create(
            user=user,
            trip_member=member,
            title="Holiday Adventure",
            destination=destination,
            start_date="2025-01-01",
            end_date="2025-01-10",
            notes="Excited for this trip!"
        )
        self.assertEqual(str(trip), "john - (Kruger Park)")
