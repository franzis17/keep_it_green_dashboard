from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElectricityEmissionViewSet

router = DefaultRouter()
router.register(r'emissions', ElectricityEmissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
