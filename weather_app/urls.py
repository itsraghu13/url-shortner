from django.urls import path
from weather_app.views import weather

urlpatterns = [
    path('weather',weather,name="weather")
]
