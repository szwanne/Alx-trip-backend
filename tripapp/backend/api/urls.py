from django.urls import path
from . import views


urlpatterns = [
    path('trips/', views.UserProfileList.as_view())
]
