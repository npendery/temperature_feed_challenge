import pytest

from loft_temperature_feed_app.models import Temperature

def test_temperature_value():
    temperature = Temperature(value=20.0, timestamp="2021-10-10 10:10:10")
    assert temperature.value == 20.0

def test_temperature_timestamp():
    temperature = Temperature(value=20.0, timestamp="2021-10-10 10:10:10")
    assert temperature.timestamp == "2021-10-10 10:10:10"

def test_temperature_str():
    temperature = Temperature(value=20.0, timestamp="2021-10-10 10:10:10")
    assert str(temperature) == "20.0 at 2021-10-10 10:10:10"
