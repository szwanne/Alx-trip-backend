from django.urls import path
from . import views


urlpatterns = [
    path('trips/', views.UserProfileListCreate.as_view())
]
