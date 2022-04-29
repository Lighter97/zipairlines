import decimal

from django.conf import settings

# import math


class Airplane:
    def __init__(self, airplane_id: int, passengers: int):
        self._airplane_id = self._validate_id(airplane_id)
        self._passengers = self._validate_passengers(passengers)

    def _validate_id(self, airplane_id: int) -> int:
        if airplane_id < 0:
            raise ValueError("Airplane id must be greater than 0")
        return airplane_id

    def _validate_passengers(self, passengers: int) -> int:
        if passengers < 0:
            raise ValueError("Passengers must be greater than 0")
        return passengers

    def fuel_capacity(self) -> decimal.Decimal:
        return round(self._airplane_id * settings.DEFAULT_FUEL_CAPACITY, 3)

    def fuel_by_passenger(self) -> decimal.Decimal:
        return round(self._passengers * settings.FUEL_BY_PASSENGER, 3)

    def fuel_by_minute(self) -> decimal.Decimal:
        # Pure multiplication instead of logarithm
        # because of unanswered question
        return round(
            decimal.Decimal(self._airplane_id * settings.MULTIPLY_VALUE),
            3,
        )

    def fuel_required_total(self) -> decimal.Decimal:
        return round(self.fuel_by_minute() + self.fuel_by_passenger(), 3)

    def maximum_minutes(self) -> decimal.Decimal:
        return round(self.fuel_capacity() / self.fuel_required_total(), 3)
