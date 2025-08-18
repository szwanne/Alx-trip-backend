from django.urls import path
from . import views


urlpatterns = [
    # UserProfile endpoints
    path('profiles/', views.UserProfileListCreate.as_view(),
         name='userprofile-list-create'),
    path('profiles/<int:pk>', views.UserProfileRetrieveUpdateDestroy.as_view(),
         name='userprofile-detail'),
    # Destinations
    path('destinations/', views.DestinationListCreate.as_view(),
         name='destination-list-create'),
    # Trip endpoints
    path('trips/', views.TripListCreate.as_view(), name='trip-list-create'),
    path('trips/<int:pk>/', views.TripRetrieveUpdateDestroy.as_view(),
         name='trip-detail'),
]
