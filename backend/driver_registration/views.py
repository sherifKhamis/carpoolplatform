from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Driver

# Create your views here.

@csrf_exempt
def register_driver(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        driver = Driver.objects.create(
            license_number=data['license_number'],
            vehicle_model=data['vehicle_model'],
            seats_available=data['seats_available'],
            make=data['make'],
            model=data['model'],
            year=data['year'],
            color=data.get('color', ''),
            license_plate=data['license_plate'],
            seats=data['seats'],
        )
        return JsonResponse({'message': 'Driver registered successfully!'}, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
