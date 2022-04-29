from django.conf import settings

from rest_framework import serializers

from airplanes.utils import Airplane


class AirplaneSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    passengers = serializers.IntegerField()

    fuel_per_minute = serializers.SerializerMethodField()
    maximum_minutes = serializers.SerializerMethodField()

    class Meta:
        fields = ("id", "passengers", "fuel_per_minute", "maximum_minutes")

    def get_fuel_per_minute(self, obj):
        return Airplane(obj.get("id"), obj.get("passengers")).fuel_by_minute()

    def get_maximum_minutes(self, obj):
        return Airplane(obj.get("id"), obj.get("passengers")).maximum_minutes()


class FleetSerializer(serializers.Serializer):
    airplanes = AirplaneSerializer(
        many=True,
        max_length=settings.AIRPLANES_LIMIT,
    )

    class Meta:
        fields = ("airplanes",)
