from django.urls import path
from .views import (
    CarListView, CarDetailView, BookingListView, BookingDetailView,
    RegisterView, LoginView, PasswordResetRequestView, PasswordResetView
)

urlpatterns = [
    # Car Endpoints
    path('api/cars/', CarListView.as_view(), name='car-list'),  # List all cars
    path('api/cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),  # Car details

    # Booking Endpoints
    path('api/bookings/', BookingListView.as_view(), name='booking-list'),  # List all bookings
    path('api/bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),  # Booking details

    # Authentication Endpoints
    path('api/register/', RegisterView.as_view(), name='register'),  # Register user
    path('api/login/', LoginView.as_view(), name='login'),  # Login user

    # Password Reset Endpoints
    path('api/password-reset-request/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('api/password-reset/', PasswordResetView.as_view(), name='password-reset'),
]
