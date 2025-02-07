from django.shortcuts import render
from rest_framework import viewsets
from .models import ElectricityEmission
from .serializers import ElectricityEmissionSerializer

class ElectricityEmissionViewSet(viewsets.ModelViewSet):
    queryset = ElectricityEmission.objects.all()
    serializer_class = ElectricityEmissionSerializer

# Create your views here.
def get_emissions(request):
    # Create a new entry
    emission = ElectricityEmission.objects.create(
        kwh_used=1000
    )
    
    # Get CO2 emissions
    co2_emissions = emission.calculate_emissions()
    
    # Get all emissions for display
    all_emissions = ElectricityEmission.objects.all()
    total_emissions = sum(e.calculate_emissions() for e in all_emmisions)


def record_electricity(request):
    monthly_kwh = 1000
    
    usage = ElectricityEmission.objects.create(
        kwh_used=monthly_kwh
    )
    
    emissions = usage.calculate_emissions()
