from rest_framework import serializers
from .models import ElectricityEmission

class ElectricityEmissionSerializer(serializers.ModelSerializer):
    co2_emissions = serializers.SerializerMethodField()
    
    class Meta:
        model = ElectricityEmission
        fields = ['id', 'kwh_used', 'date', 'co2_emissions']
    
    def get_co2_emissions(self, obj):
        return round(obj.calculate_emissions(), 2)
