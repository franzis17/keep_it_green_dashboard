from django.contrib import admin
from .models import ElectricityEmission

# Register your models here.
@admin.register(ElectricityEmission)
class ElectricityEmissionAdmin(admin.ModelAdmin):
    list_display = ('kwh_used', 'date', 'calculate_emissions')
    list_filter = ('date',)
    search_fields = ('kwh_used', 'date')
