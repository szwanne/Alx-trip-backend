from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    # shows these columns in the admin site
    list_display = ('user', 'date_joined')
    # allows searching by username and/or email
    search_fields = ('user__username', 'user__email')


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
