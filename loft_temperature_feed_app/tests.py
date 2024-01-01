from django.test import TestCase

from loft_temperature_feed_app.models import Temperature

class TemperatureModelTests(TestCase):
    def test_temperature_str(self):
        temperature = Temperature(temperature=20.0, timestamp="2021-10-10 10:10:10")
        self.assertEqual(str(temperature), "20.0 at 2021-10-10 10:10:10")
