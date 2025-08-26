from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Booking(models.Model):
    type = models.CharField(max_length=100)
    detail = models.TextField(max_length=200, blank=True)
    booking_date = models.DateTimeField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name="bookings")

    def __str__(self):
        return self.user.username


class Activity(models.Model):
    destination = models.ForeignKey("Destination",
                                    on_delete=models.CASCADE,
                                    related_name="activities",
                                    null=True, blank=True)

    name = models.CharField(max_length=100, unique=False)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    image_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        dest = self.destination.name if self.destination else "No destination"
        return f"{self.name} ({dest})"


class FlightOffer(models.Model):
    airline = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=20)
    departure_airport = models.CharField(max_length=100)
    arrival_airport = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cabin_class = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.airline} {self.flight_number} ({self.departure_airport} > {self.arrival_airport})"


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.location})"


class Destination(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    flightoffer = models.ForeignKey(FlightOffer, on_delete=models.CASCADE,
                                    related_name="flightoffers",
                                    null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,
                              related_name="hotels",
                              null=True, blank=True)

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


class Weather(models.Model):
    location = models.CharField(max_length=200)
    date = models.DateField()
    temperature = models.FloatField()
    condition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.location} {self.date} - {self.condition}"


class Itinerary(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="itineraries")
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    flight_offer = models.ForeignKey(
        FlightOffer, on_delete=models.SET_NULL, null=True, blank=True)
    hotel = models.ForeignKey(
        Hotel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Itinerary: {self.name} ({self.start_date} > {self.end_date})"


class ItineraryItem(models.Model):
    itinerary = models.ForeignKey(
        Itinerary, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.title} on {self.date}"
