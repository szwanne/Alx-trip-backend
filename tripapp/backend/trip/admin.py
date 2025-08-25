from django.contrib import admin
from .models import UserProfile, Destination, Trip, Activity, TripMember, Booking, FlightOffer, Hotel, Weather, Itinerary, ItineraryItem


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('type', 'detail', 'booking_date')


class UserProfileAdmin(admin.ModelAdmin):
    # shows these columns in the admin site
    list_display = ('user', 'date_joined')
    # allows searching by username and/or email
    search_fields = ('user__username', 'user__email')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'date', 'image_url')
    search_fields = ('name',)


@admin.register(FlightOffer)
class FlightOfferAdmin(admin.ModelAdmin):
    list_display = ('airline', 'flight_number', 'departure_airport',
                    'arrival_airport', 'departure_time', 'arrival_time', 'cabin_class', 'price')
    search_fields = ('flight_number', 'arrival_airport',
                     'departure_time', 'arrival_time', 'price')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'check_in_date',
                    'check_out_date', 'price_per_night', 'rating')
    search_fields = ('name', 'location', 'check_in_date',
                     'check_out_date', 'price_per_night')


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'image_url')
    search_fields = ('name', 'country')


@admin.register(TripMember)
class TripMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'destination_id',
                    'start_date', 'end_date', 'user')
    search_fields = ('title', 'destination', 'user__username')


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('location', 'date', 'condition', 'temperature')


@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date',
                    'end_date', 'flight_offer', 'hotel')


@admin.register(ItineraryItem)
class ItineraryItemAdmin(admin.ModelAdmin):
    list_display = ('itinerary', 'title',
                    'description', 'date', 'start_time', 'end_time', 'location')


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
