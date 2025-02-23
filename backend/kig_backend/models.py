from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from decimal import Decimal

class ElectricityEmission(models.Model):
    """
    Record electricity usage and automatically calculate CO2 Emissions
    """
    
    # Electricity used in killowatt-hours (kWh)
    kwh_used = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Electricity used in kilowatt-hours (kWh)"
    )
    
    date = models.DateField(default=timezone.now)
    
    # Average emission factor in Perth, WA is 0.67
    EMISSION_FACTOR = Decimal('0.67')
    

    class Meta:
        ordering = ['-date']
    
    
    def calculate_emissions(self):
        """Calculate CO2 emissions in kilograms"""
        return float(self.kwh_used * self.EMISSION_FACTOR)
    
    def __str__(self):
        return f"{self.kwh_used}kWh = {self.calculate_emissions():.2f}kg CO2"
