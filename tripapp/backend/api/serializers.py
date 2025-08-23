from rest_framework import serializers
from django.contrib.auth.models import User
from trip.models import UserProfile, Activity, Destination, TripMember, Trip, Booking
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
