from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # Bookings endpoints
    path('bookings/', views.BookingListCreate.as_view(),
         name='bookings-list-create'),
    path('bookings/<int:pk>/',
         views.BookingRetrieveUpdateDestroy.as_view(), name='booking-details'),
    # UserProfile endpoints
    path('profiles/', views.UserProfileListCreate.as_view(),
         name='userprofile-list-create'),
    path('profiles/<int:pk>', views.UserProfileRetrieveUpdateDestroy.as_view(),
         name='userprofile-detail'),
    # Activity endpoints
    path('activity/', views.ActivityListCreate.as_view(),
         name='activity-list-create'),
    path('activity/<int:pk>/',
         views.ActivityRetrieveUpdateDestroy.as_view(), name='activity-detail'),
    # Destinations endpoints
    path('destinations/', views.DestinationListCreate.as_view(),
         name='destination-list-create'),
    path('destinations/<int:pk>/',
         views.DestinationRetrieveUpdateDestroy.as_view(), name='destination-detail'),
    path('destinations/<int:pk>/activities/',
         views.DestinationActivitiesList.as_view(), name='destination-activities'),
    # Trip endpoints
    path('trips/', views.TripListCreate.as_view(), name='trip-list-create'),
    path('trips/<int:pk>/', views.TripRetrieveUpdateDestroy.as_view(),
         name='trip-detail'),
    # Trip members endpoints
    path('trip-members/', views.TripMemberListCreate.as_view(),
         name='trip-members-create-list'),
    path('trip-members/<int:pk>/',
         views.TripMemberRetrieveUpdateDestroy.as_view(), name='trip-member-detail'),
    # Auth endpoints
    path('signup/', views.signup),
    path('login/', views.login),
]
