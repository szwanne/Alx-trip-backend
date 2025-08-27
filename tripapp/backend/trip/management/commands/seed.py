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
UNSPLASH_IMAGES_HOTEL = [
    "https://images.unsplash.com/photo-1559599101-b8b6b2c8f3b3",
    "https://images.unsplash.com/photo-1501117716987-c8e1ecb210f3",
    "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2",
    "https://images.unsplash.com/photo-1578683010236-d716f9a3f461",
    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c",
    "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267",
    "https://images.unsplash.com/photo-1543353071-087092ec393a",
    "https://images.unsplash.com/photo-1555992336-03a23c7b20d2",
    "https://images.unsplash.com/photo-1541542684-4e5b7e23f56d",
    "https://images.unsplash.com/photo-1525610553991-2bede1a236e2",
    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4",
    "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe",
    "https://images.unsplash.com/photo-1590490358125-86b3d4c2f2db",
    "https://images.unsplash.com/photo-1551907234-85d1c6b7f2bc",
    "https://images.unsplash.com/photo-1582719478181-0d37f1d2e4d5",
    "https://images.unsplash.com/photo-1600585154336-8f9f8f7f1c2b",
    "https://images.unsplash.com/photo-1560448204-5f3f9d6b4e1a",
    "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267"
    "https://images.unsplash.com/photo-1542317854-25194f73ed36",
    "https://images.unsplash.com/photo-1590490358111-0b1f3f4e2f7d",
    "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb",
    "https://images.unsplash.com/photo-1568495248636-643574b29b46",
    "https://images.unsplash.com/photo-1501117716987-c8e2eaa7a034",
    "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb",
    "https://images.unsplash.com/photo-1560448204-5f3f9d6b4e1a",
    "https://images.unsplash.com/photo-1590490358125-86b3d4c2f2db",
    "https://images.unsplash.com/photo-1582719478181-0d37f1d2e4d5",
    "https://images.unsplash.com/photo-1560347876-aeef00ee58a1",
    "https://images.unsplash.com/photo-1501117716987-c8e2eaa7a034",
    "https://images.unsplash.com/photo-1582719478181-0d37f1d2e4d5",
    "https://images.unsplash.com/photo-1600585154336-8f9f8f7f1c2b",
    "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267",
    "https://images.unsplash.com/photo-1542317854-25194f73ed36",
    "https://images.unsplash.com/photo-1560448204-5f3f9d6b4e1a",
    "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb",
    "https://images.unsplash.com/photo-1600585154336-8f9f8f7f1c2b",
    "https://images.unsplash.com/photo-1560347876-aeef00ee58a1",
    "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267",
    "https://images.unsplash.com/photo-1582719478181-0d37f1d2e4d5",
    "https://images.unsplash.com/photo-1542317854-25194f73ed36",
    "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6",
    "https://images.unsplash.com/photo-1517816743773-6e0fd518b4a6",
    "https://images.unsplash.com/photo-1530541930197-c0f2e6f4c2a2",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
    "https://images.unsplash.com/photo-1558980664-10d15d5e3e39",
    "https://images.unsplash.com/photo-1504711434969-e33886168f5c",
    "https://images.unsplash.com/photo-1541872703-141b11203f36",
    "https://images.unsplash.com/photo-1533577116850-9cc66cad8a9b",
    "https://images.unsplash.com/photo-1524524152507-9d1740ebd4a1",
    "https://images.unsplash.com/photo-1523473827538-0c7f3dc6597b", "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb",
    "https://images.unsplash.com/photo-1568495248636-643574b29b46",
    "https://images.unsplash.com/photo-1501117716987-c8e2eaa7a034",
    "https://images.unsplash.com/photo-1560448204-5f3f9d6b4e1a",
    "https://images.unsplash.com/photo-1590490358125-86b3d4c2f2db",
    "https://images.unsplash.com/photo-1582719478181-0d37f1d2e4d5",
    "https://images.unsplash.com/photo-1560347876-aeef00ee58a1",
    "https://images.unsplash.com/photo-1600585154336-8f9f8f7f1c2b",
    "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267",
    "https://images.unsplash.com/photo-1542317854-25194f73ed36",
    "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6",
    "https://images.unsplash.com/photo-1517816743773-6e0fd518b4a6",
    "https://images.unsplash.com/photo-1530541930197-c0f2e6f4c2a2",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
    "https://images.unsplash.com/photo-1558980664-10d15d5e3e39",
    "https://images.unsplash.com/photo-1504711434969-e33886168f5c",
    "https://images.unsplash.com/photo-1541872703-141b11203f36",
    "https://images.unsplash.com/photo-1533577116850-9cc66cad8a9b",
    "https://images.unsplash.com/photo-1524524152507-9d1740ebd4a1",
    "https://images.unsplash.com/photo-1523473827538-0c7f3dc6597b"

]

UNSPLASH_IMAGES_ACTIVITY = [
    "https://images.unsplash.com/photo-1520975918318-8c6b3ce04899",
    "https://images.unsplash.com/photo-1508973372-2d0b7b1f80ef",
    "https://images.unsplash.com/photo-1472653431158-6364773b2a56",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "https://images.unsplash.com/photo-1533681801679-64a07f1e2e4b",
    "https://images.unsplash.com/photo-1491553895911-0055eca6402d",
    "https://images.unsplash.com/photo-1543353071-087092ec393a",
    "https://images.unsplash.com/photo-1555992336-03a23c7b20d2",
    "https://images.unsplash.com/photo-1541542684-4e5b7e23f56d",
    "https://images.unsplash.com/photo-1516939884455-1445c8652f83",
    "https://images.unsplash.com/photo-1526481280691-906f1f1f7c1a",
    "https://images.unsplash.com/photo-1508672019048-805c876b67e2",
    "https://images.unsplash.com/photo-1529635984450-3f20211fbd50",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    "https://images.unsplash.com/photo-1518609878373-06d740f60d8b",
    "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c",
    "https://images.unsplash.com/photo-1534258936925-c58e2e42d3fa",
    "https://images.unsplash.com/photo-1517841905240-472988babdf9",
    "https://images.unsplash.com/photo-1541508184032-7db923f5b3f0",
    "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6",
    "https://images.unsplash.com/photo-1517816743773-6e0fd518b4a6",
    "https://images.unsplash.com/photo-1530541930197-c0f2e6f4c2a2",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
    "https://images.unsplash.com/photo-1558980664-10d15d5e3e39",
    "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6",
    "https://images.unsplash.com/photo-1504711434969-e33886168f5c",
    "https://images.unsplash.com/photo-1541872703-141b11203f36",
    "https://images.unsplash.com/photo-1533577116850-9cc66cad8a9b",
    "https://images.unsplash.com/photo-1524524152507-9d1740ebd4a1",
    "https://images.unsplash.com/photo-1524041252511-dfd0c8bce94e",
    "https://images.unsplash.com/photo-1562007902-3f27ce5a29f9",
    "https://images.unsplash.com/photo-1526045612212-70caf35c14df",
    "https://images.unsplash.com/photo-1523473827538-0c7f3dc6597b",
    "https://images.unsplash.com/photo-1501700493786-3e4d06fa12a5",
    "https://images.unsplash.com/photo-1519681393784-d120267933ba",
    "https://images.unsplash.com/photo-1493244040629-496f6d136cc3",
    "https://images.unsplash.com/photo-1516483638261-f4dbaf036963",
    "https://images.unsplash.com/photo-1542728928-5c1c812a0a1e",
    "https://images.unsplash.com/photo-1519125323398-675f0ddb6308",
    "https://images.unsplash.com/photo-1499744937866-d9e0d7eb5562",
    "https://images.unsplash.com/photo-1473187983305-f615310e7daa",
    "https://images.unsplash.com/photo-1529635984450-3f20211fbd50",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    "https://images.unsplash.com/photo-1518609878373-06d740f60d8b",
    "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c",
    "https://images.unsplash.com/photo-1534258936925-c58e2e42d3fa",
    "https://images.unsplash.com/photo-1517841905240-472988babdf9",
    "https://images.unsplash.com/photo-1541508184032-7db923f5b3f0",
    "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6",
    "https://images.unsplash.com/photo-1517816743773-6e0fd518b4a6",
    "https://images.unsplash.com/photo-1530541930197-c0f2e6f4c2a2",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
    "https://images.unsplash.com/photo-1558980664-10d15d5e3e39",
    "https://images.unsplash.com/photo-1504711434969-e33886168f5c",
    "https://images.unsplash.com/photo-1541872703-141b11203f36",
    "https://images.unsplash.com/photo-1533577116850-9cc66cad8a9b",
    "https://images.unsplash.com/photo-1524524152507-9d1740ebd4a1",
    "https://images.unsplash.com/photo-1523473827538-0c7f3dc6597b",
    "https://images.unsplash.com/photo-1501700493786-3e4d06fa12a5",
    "https://images.unsplash.com/photo-1519681393784-d120267933ba",
    "https://images.unsplash.com/photo-1493244040629-496f6d136cc3",
    "https://images.unsplash.com/photo-1516483638261-f4dbaf036963",
    "https://images.unsplash.com/photo-1542728928-5c1c812a0a1e",
    "https://images.unsplash.com/photo-1519125323398-675f0ddb6308",
    "https://images.unsplash.com/photo-1499744937866-d9e0d7eb5562",
    "https://images.unsplash.com/photo-1473187983305-f615310e7daa",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    "https://images.unsplash.com/photo-1518609878373-06d740f60d8b",
    "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c",
    "https://images.unsplash.com/photo-1534258936925-c58e2e42d3fa",
    "https://images.unsplash.com/photo-1517841905240-472988babdf9",
    "https://images.unsplash.com/photo-1541508184032-7db923f5b3f0",
    "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6",
    "https://images.unsplash.com/photo-1517816743773-6e0fd518b4a6",
    "https://images.unsplash.com/photo-1530541930197-c0f2e6f4c2a2",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
    "https://images.unsplash.com/photo-1558980664-10d15d5e3e39",
    "https://images.unsplash.com/photo-1504711434969-e33886168f5c",
    "https://images.unsplash.com/photo-1541872703-141b11203f36",
    "https://images.unsplash.com/photo-1533577116850-9cc66cad8a9b",
    "https://images.unsplash.com/photo-1524524152507-9d1740ebd4a1",
    "https://images.unsplash.com/photo-1523473827538-0c7f3dc6597b"
]

UNSPLASH_IMAGES_DESTINATION = [
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    "https://images.unsplash.com/photo-1519681393784-d120267933ba",
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
    "https://images.unsplash.com/photo-1469474968028-56623f02e42e",
    "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0",
    "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800",
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
    "https://images.unsplash.com/photo-1543248939-ff40856f65d4",
    "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05",
    "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
    "https://images.unsplash.com/photo-1441829266145-6d4bfbd38eb4",
    "https://images.unsplash.com/photo-1469474968028-56623f02e42e",
    "https://images.unsplash.com/photo-1465101162946-4377e57745c3",
    "https://images.unsplash.com/photo-1470770841072-f978cf4d019e",
    "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",
    "https://images.unsplash.com/photo-1508672019048-805c876b67e2",
    "https://images.unsplash.com/photo-1492684223066-81342ee5ff30",
    "https://images.unsplash.com/photo-1496307042754-b4aa456c4a2d",
    "https://images.unsplash.com/photo-1508672019048-805c876b67e2",
    "https://images.unsplash.com/photo-1520975918318-8c6b3ce04899",
    "https://images.unsplash.com/photo-1520975918318-8c6b3ce04899",
    "https://images.unsplash.com/photo-1519681393784-d120267933ba",
    "https://images.unsplash.com/photo-1497493292307-31c376b6e479",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    "https://images.unsplash.com/photo-1518609878373-06d740f60d8b",
    "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c",
    "https://images.unsplash.com/photo-1534258936925-c58e2e42d3fa",
    "https://images.unsplash.com/photo-1517841905240-472988babdf9",
    "https://images.unsplash.com/photo-1541508184032-7db923f5b3f0",
    "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6",
    "https://images.unsplash.com/photo-1517816743773-6e0fd518b4a6",
    "https://images.unsplash.com/photo-1530541930197-c0f2e6f4c2a2",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
    "https://images.unsplash.com/photo-1558980664-10d15d5e3e39",
    "https://images.unsplash.com/photo-1504711434969-e33886168f5c",
    "https://images.unsplash.com/photo-1541872703-141b11203f36",
    "https://images.unsplash.com/photo-1533577116850-9cc66cad8a9b",
    "https://images.unsplash.com/photo-1524524152507-9d1740ebd4a1",
    "https://images.unsplash.com/photo-1523473827538-0c7f3dc6597b",
    "https://images.unsplash.com/photo-1501700493786-3e4d06fa12a5",
    "https://images.unsplash.com/photo-1519681393784-d120267933ba",
    "https://images.unsplash.com/photo-1493244040629-496f6d136cc3",
    "https://images.unsplash.com/photo-1516483638261-f4dbaf036963",
    "https://images.unsplash.com/photo-1542728928-5c1c812a0a1e",
    "https://images.unsplash.com/photo-1519125323398-675f0ddb6308",
    "https://images.unsplash.com/photo-1499744937866-d9e0d7eb5562",
    "https://images.unsplash.com/photo-1473187983305-f615310e7daa",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    "https://images.unsplash.com/photo-1518609878373-06d740f60d8b",
    "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c",
    "https://images.unsplash.com/photo-1534258936925-c58e2e42d3fa",
    "https://images.unsplash.com/photo-1517841905240-472988babdf9",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    "https://images.unsplash.com/photo-1518609878373-06d740f60d8b",
    "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c",
    "https://images.unsplash.com/photo-1534258936925-c58e2e42d3fa",
    "https://images.unsplash.com/photo-1517841905240-472988babdf9",
    "https://images.unsplash.com/photo-1541508184032-7db923f5b3f0",
    "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6",
    "https://images.unsplash.com/photo-1517816743773-6e0fd518b4a6",
    "https://images.unsplash.com/photo-1530541930197-c0f2e6f4c2a2",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
    "https://images.unsplash.com/photo-1558980664-10d15d5e3e39",
    "https://images.unsplash.com/photo-1504711434969-e33886168f5c",
    "https://images.unsplash.com/photo-1541872703-141b11203f36",
    "https://images.unsplash.com/photo-1533577116850-9cc66cad8a9b",
    "https://images.unsplash.com/photo-1524524152507-9d1740ebd4a1"

]


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
                image_url=random.choice(UNSPLASH_IMAGES_HOTEL),
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
                image_url=random.choice(UNSPLASH_IMAGES_DESTINATION),
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
                    image_url=random.choice(UNSPLASH_IMAGES_ACTIVITY),
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
