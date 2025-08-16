from django.urls import path
from . import views


urlpatterns = [
    path('trips/', views.UserProfileListCreate.as_view()),
    path('trips/<int:pk>', views.UserProfileRetrieveUpdateDestroy.as_view())
]
