from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model with an additional 'role' field to distinguish between drivers and passengers.
    """
    ROLE_CHOICES = [
        ('driver', 'Driver'),
        ('passenger', 'Passenger'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='passenger')

    def __str__(self):
        return self.username

class DriverProfile(models.Model):
    """
    Profile for drivers. Here, vehicle-specific information and other driver-related details can be stored.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='driver_profile')
    license_number = models.CharField(max_length=50, blank=True, null=True, help_text="Driver's license number")
    vehicle_model = models.CharField(max_length=100, blank=True, null=True, help_text="Vehicle model")
    seats_available = models.PositiveIntegerField(default=0, help_text="Number of available seats")

    def __str__(self):
        return f"Driver: {self.user.username}"

class PassengerProfile(models.Model):
    """
    Profile for passengers. Passenger-specific information, such as ratings or preferences, can be stored here.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='passenger_profile')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.00, help_text="Passenger rating")

    def __str__(self):
        return f"Passenger: {self.user.username}"
