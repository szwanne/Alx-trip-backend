from rest_framework import serializers
from trip.models import UserProfile, Activity, Destination, TripMember, Trip


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'date_joined']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'description', 'date']


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'name', 'country', 'description']


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
