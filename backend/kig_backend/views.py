from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import ElectricityEmission
from .serializers import ElectricityEmissionSerializer

# Create your views here.
class ElectricityEmissionViewSet(viewsets.ModelViewSet):
    queryset = ElectricityEmission.objects.all()
    serializer_class = ElectricityEmissionSerializer
    
    def list(self, request):
        emissions = self.get_queryset()
        serializer = self.get_serializer(emissions, many=True)
        total_emissions = sum(emission.calculate_emissions() for emission in emissions)
        
        return Response({
            'emissions': serializer.data,
            'total_emissions': round(total_emissions, 2)
        })
