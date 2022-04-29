from decimal import Decimal

from django.conf import settings
from django.test import SimpleTestCase

from airplanes.utils import Airplane


class AirplaneTests(SimpleTestCase):
    def setUp(self):
        self.airplane = Airplane(airplane_id=2, passengers=100)

    def test__fuel_capacity(self):
        self.assertEqual(self.airplane.fuel_capacity(), round(Decimal(2 * 200), 3))

    def test__fuel_by_passenger(self):
        self.assertEqual(
            self.airplane.fuel_by_passenger(),
            round(Decimal(100 * settings.FUEL_BY_PASSENGER), 3),
        )

    def test__fuel_by_minute(self):
        self.assertEqual(
            self.airplane.fuel_by_minute(),
            round(Decimal(2 * settings.MULTIPLY_VALUE), 3),
        )

    def test__fuel_required_total(self):
        self.assertEqual(
            self.airplane.fuel_required_total(),
            round(
                Decimal(2 * settings.MULTIPLY_VALUE)
                + Decimal(100 * settings.FUEL_BY_PASSENGER),
                3,
            ),
        )

    def test__maximum_minutes(self):
        self.assertEqual(
            self.airplane.maximum_minutes(),
            round(
                Decimal(
                    400
                    / (2 * settings.MULTIPLY_VALUE + 100 * settings.FUEL_BY_PASSENGER)
                ),
                3,
            ),
        )
