import random
from datetime import timedelta, date, datetime
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from trip.models import (
    Booking, UserProfile, Activity, FlightOffer, Hotel, Destination,
    TripMember, Trip, Weather, Itinerary, ItineraryItem
)
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = "Seed the database with sample data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # ✅ Users
        users = []
        for i in range(10):
            user, created = User.objects.get_or_create(
                username=fake.user_name() + str(i),
                defaults={"email": fake.email()}
            )
            if created:
                user.set_password("password123")
                user.save()
            users.append(user)

        # ✅ Bookings + UserProfiles
        bookings = []
        for user in users:
            booking = Booking.objects.create(
                type=random.choice(["Flight", "Hotel", "Activity"]),
                detail=fake.text(),
                booking_date=fake.date_time_this_year()
            )
            UserProfile.objects.get_or_create(user=user, booking=booking)
            bookings.append(booking)

        # ✅ Flights
        flights = []
        for _ in range(20):
            flights.append(FlightOffer.objects.create(
                airline=fake.company(),
                flight_number=f"FL{random.randint(100, 999)}",
                departure_airport=fake.city(),
                arrival_airport=fake.city(),
                departure_time=fake.date_time_this_month(),
                arrival_time=fake.date_time_this_month(),
                price=round(random.uniform(100, 1500), 2),
                cabin_class=random.choice(["Economy", "Business", "First"])
            ))

        # ✅ Hotels
        hotels = []
        for _ in range(20):
            hotels.append(Hotel.objects.create(
                name=fake.company(),
                location=fake.city(),
                image_url=fake.image_url(),
                check_in_date=date.today(),
                check_out_date=date.today() + timedelta(days=random.randint(1, 10)),
                price_per_night=round(random.uniform(50, 500), 2),
                rating=random.uniform(2, 5),
            ))

        # ✅ Destinations
        destinations = []
        for _ in range(15):
            destinations.append(Destination.objects.create(
                name=fake.city(),
                country=fake.country(),
                description=fake.text(),
                image_url=fake.image_url(),
                flightoffer=random.choice(flights),
                hotel=random.choice(hotels)
            ))

        # ✅ Activities
        for dest in destinations:
            for _ in range(3):
                Activity.objects.create(
                    destination=dest,
                    name=fake.word().title(),
                    description=fake.sentence(),
                    date=fake.date_time_this_year(),
                    image_url=fake.image_url(),
                )

        # ✅ Trip Members
        members = []
        for _ in range(20):
            members.append(TripMember.objects.create(
                name=fake.name(),
                email=fake.unique.email()
            ))

        # ✅ Trips
        trips = []
        for user in users:
            for _ in range(2):
                trips.append(Trip.objects.create(
                    user=user,
                    trip_member=random.choice(members),
                    title=fake.sentence(nb_words=3),
                    destination=random.choice(destinations),
                    start_date=date.today(),
                    end_date=date.today() + timedelta(days=random.randint(3, 14)),
                    notes=fake.text(),
                ))

        # ✅ Weather
        for dest in destinations:
            for _ in range(5):
                Weather.objects.create(
                    location=dest.name,
                    date=date.today() + timedelta(days=random.randint(0, 7)),
                    temperature=random.uniform(10, 35),
                    condition=random.choice(
                        ["Sunny", "Rainy", "Cloudy", "Stormy"])
                )

        # ✅ Itineraries
        itineraries = []
        for user in users:
            itinerary = Itinerary.objects.create(
                user=user,
                name=f"{user.username}'s Trip",
                start_date=date.today(),
                end_date=date.today() + timedelta(days=5),
                flight_offer=random.choice(flights),
                hotel=random.choice(hotels),
            )
            itineraries.append(itinerary)

            # ✅ Itinerary Items
            for _ in range(3):
                ItineraryItem.objects.create(
                    itinerary=itinerary,
                    title=fake.sentence(nb_words=3),
                    description=fake.text(),
                    date=date.today() + timedelta(days=random.randint(0, 5)),
                    start_time=datetime.now().time(),
                    end_time=datetime.now().time(),
                    location=fake.city()
                )

        self.stdout.write(self.style.SUCCESS(
            "✅ Database successfully seeded!"))
