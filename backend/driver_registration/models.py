from django.db import models

class Driver(models.Model):
    license_number = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=100)
    seats_available = models.PositiveIntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30, blank=True)
    license_plate = models.CharField(max_length=20)
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.license_number} - {self.vehicle_model}"
