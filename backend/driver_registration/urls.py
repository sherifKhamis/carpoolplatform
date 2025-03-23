# filepath: /Users/sherifkhamis/Projects/carpoolplatform/backend/driver_registration/urls.py
from django.urls import path
from .views import register_driver

urlpatterns = [
    path('register-driver/', register_driver, name='register_driver'),
]