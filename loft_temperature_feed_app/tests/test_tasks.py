import pytest
from unittest.mock import patch

from loft_temperature_feed_app.utils import ExternalApi
from loft_temperature_feed_app.tasks import ingest_temperatures

def test_ingest_temperatures():
    mock_target = "loft_temperature_feed_app.utils.ExternalApi.ingest_temperatures"
    with patch(mock_target) as mock_ingest:
        ingest_temperatures()
        mock_ingest.assert_called_once_with()
