from django.urls import path
from .views import random_number, weather_info,random_password

urlpatterns = [
    path('generate-password',random_password),
    path('generate-number',random_number),
    path('weather/',weather_info),
]
