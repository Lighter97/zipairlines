from django.urls import path

from airplanes.views import calculate_fleet


app_name = "airplanes"

urlpatterns = [path("calculate_fleet/", calculate_fleet, name="airplanes")]
