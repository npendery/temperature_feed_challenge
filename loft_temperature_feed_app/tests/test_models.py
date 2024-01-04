import pytest

from loft_temperature_feed_app.models import Temperature


def test_temperature_value():
    """
    The db column for value should be a float.
    """
    temperature = Temperature(value=20.0, timestamp="2021-10-10 10:10:10")
    assert temperature.value == 20.0


def test_temperature_timestamp():
    """
    The db column for timestamp should be a datetime.
    """
    temperature = Temperature(value=20.0, timestamp="2021-10-10 10:10:10")
    assert temperature.timestamp == "2021-10-10 10:10:10"


def test_temperature_str():
    """
    The str method should return a string representation of the Temperature object.
    """
    temperature = Temperature(value=20.0, timestamp="2021-10-10 10:10:10")
    assert str(temperature) == "20.0 at 2021-10-10 10:10:10"
