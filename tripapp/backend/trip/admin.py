from django.contrib import admin
from .models import UserProfile, Destination, Trip, Activity, TripMember, Booking


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
    list_display = ('name', 'description', 'date')


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'description')


@admin.register(TripMember)
class TripMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'destination_id',
                    'start_date', 'end_date', 'user')
    search_fields = ('title', 'destination', 'user__username')


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
