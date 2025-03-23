from django.db import models
from users.models import DriverProfile, PassengerProfile

class Car(models.Model):
    """
    Model representing a car used in the carpool system.
    """
    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE, related_name='cars')
    make = models.CharField(max_length=50, help_text="Car manufacturer")
    model = models.CharField(max_length=50, help_text="Car model")
    year = models.PositiveIntegerField(help_text="Year of manufacture")
    color = models.CharField(max_length=30, blank=True, null=True, help_text="Car color")
    license_plate = models.CharField(max_length=20, help_text="Unique license plate number")
    seats = models.PositiveIntegerField(help_text="Total number of seats in the car")

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"


class Trip(models.Model):
    """
    Model representing a carpool trip.
    """
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='trips')
    origin = models.CharField(max_length=100, help_text="Starting location")
    destination = models.CharField(max_length=100, help_text="Destination")
    departure_time = models.DateTimeField(help_text="Departure date and time")
    arrival_time = models.DateTimeField(null=True, blank=True, help_text="Estimated arrival time")
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text="Price per seat")
    available_seats = models.PositiveIntegerField(help_text="Number of seats available for reservation")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Trip creation timestamp")

    def __str__(self):
        return f"Trip from {self.origin} to {self.destination} at {self.departure_time}"


class Reservation(models.Model):
    """
    Model representing a reservation for a trip made by a passenger.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='reservations')
    passenger = models.ForeignKey(PassengerProfile, on_delete=models.CASCADE, related_name='reservations')
    seats_reserved = models.PositiveIntegerField(default=1, help_text="Number of seats reserved")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', help_text="Reservation status")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Reservation creation timestamp")

    def __str__(self):
        return f"Reservation by {self.passenger.user.username} for trip {self.trip}"
