from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Activity, Destination, Trip, TripMember, FlightOffer, Hotel, Weather, Itinerary, ItineraryItem


class ActivityModelTest(TestCase):
    def test_create_activity(self):
        dest = Destination.objects.create(name="Cape Town")
        activity = Activity.objects.create(
            name="Hiking",
            description="Mountain hike",
            date=timezone.now(),
            destination=dest
        )
        self.assertEqual(str(activity), "Hiking (Cape Town)")


class DestinationModelTest(TestCase):
    def test_create_destination(self):
        destination = Destination.objects.create(
            name="Cape Town",
            country="South Africa",
            description="Beautiful coastal city"
        )
        self.assertEqual(str(destination), "Cape Town")


class TripModelTest(TestCase):
    def test_create_trip(self):
        user = User.objects.create_user(username="testuser", password="pass")
        trip_member = TripMember.objects.create(
            name="Alice", email="alice@example.com")
        dest = Destination.objects.create(
            name="Kruger Park", country="South Africa")

        trip = Trip.objects.create(
            user=user,
            trip_member=trip_member,
            title="Safari Trip",
            destination=dest,
            start_date=datetime.today().date(),
            end_date=datetime.today().date() + timedelta(days=5),
            notes="Bring binoculars"
        )
        self.assertEqual(str(trip), "testuser - (Kruger Park)")


class FlightOfferModelTest(TestCase):
    def test_flight_offer_creation(self):
        flight = FlightOffer.objects.create(
            airline="South African Airways",
            flight_number="SA123",
            departure_airport="JNB",
            arrival_airport="CPT",
            departure_time=timezone.now(),
            arrival_time=timezone.now() + timedelta(hours=2),
            price=250.00,
            cabin_class="Economy"
        )
        self.assertIn("South African Airways SA123", str(flight))


class HotelModelTest(TestCase):
    def test_hotel_creation(self):
        hotel = Hotel.objects.create(
            name="Hilton Cape Town",
            location="Cape Town",
            check_in_date=datetime.today().date(),
            check_out_date=datetime.today().date() + timedelta(days=3),
            price_per_night=150.00,
            rating=4.5
        )
        self.assertEqual(hotel.name, "Hilton Cape Town")


class WeatherModelTest(TestCase):
    def test_weather_creation(self):
        weather = Weather.objects.create(
            location="Cape Town",
            date=datetime.today().date(),
            temperature=22.5,
            condition="Sunny"
        )
        self.assertIn("Cape Town", str(weather))


class ItineraryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="pass")
        self.itinerary = Itinerary.objects.create(
            user=self.user,
            name="Cape Town Holiday",
            start_date=datetime.today().date(),
            end_date=datetime.today().date() + timedelta(days=5)
        )

    def test_itinerary_creation(self):
        self.assertIn("Cape Town Holiday", str(self.itinerary))


class ItineraryItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser2", password="pass")
        self.itinerary = Itinerary.objects.create(
            user=self.user,
            name="Safari",
            start_date=datetime.today().date(),
            end_date=datetime.today().date() + timedelta(days=5)
        )

    def test_itinerary_item_creation(self):
        item = ItineraryItem.objects.create(
            itinerary=self.itinerary,
            title="Morning Game Drive",
            description="See the Big 5",
            date=datetime.today().date(),
            start_time=datetime.now().time()
        )
        self.assertEqual(str(item), f"Morning Game Drive on {item.date}")
