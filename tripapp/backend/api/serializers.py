from rest_framework import serializers
from django.contrib.auth.models import User
from trip.models import UserProfile, Activity, Destination, TripMember, Trip, Booking, FlightOffer, Hotel, Weather, Itinerary, ItineraryItem
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Passwords must match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'type', 'detail', 'booking_date']


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'date_joined']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'description', 'date', 'image_url']


class FlightOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightOffer
        fields = ['id', 'airline', 'flight_number', 'departure_airport',
                  'arrival_airport', 'departure_time', 'arrival_time', 'cabin_class', 'price']


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'location', 'check_in_date',
                  'check_out_date', 'price_per_night', 'rating']


class DestinationSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = ['id', 'name', 'country',
                  'description', "activities", 'image_url']


class TripMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripMember
        fields = ['id', 'name', 'email']


class TripSerializer(serializers.ModelSerializer):
    # Nested serializer to show destination details
    destination = DestinationSerializer(read_only=True)
    destination_id = serializers.PrimaryKeyRelatedField(
        queryset=Destination.objects.all(), source='destination', write_only=True)

    class Meta:
        model = Trip
        fields = ['id', 'destination', 'destination_id',  'title', 'destination',
                  'start_date', 'end_date', 'notes']


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'location', 'date', 'temperature', 'condition']


class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = ['id', 'user', 'name', 'start_date',
                  'end_date', 'flight_offer', 'hotel']


class ItineraryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryItem
        fields = ['id', 'itinerary', 'title', 'description',
                  'date', 'start_time', 'end_time', 'location']
