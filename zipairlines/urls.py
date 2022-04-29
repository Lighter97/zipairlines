from django.contrib import admin
from django.urls import include, path

airplanes_urls = ([path("airplanes/", include("airplanes.urls"))], "api")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(airplanes_urls)),
]
