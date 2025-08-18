from django.contrib import admin
from .models import UserProfile, Trip


class UserProfileAdmin(admin.ModelAdmin):
    # shows these columns in the admin site
    list_display = ('user', 'date_joined')
    # allows searching by username and/or email
    search_fields = ('user__username', 'user__email')


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'start_date', 'end_date', 'user')
    search_fields = ('title', 'destination', 'user__username')


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
