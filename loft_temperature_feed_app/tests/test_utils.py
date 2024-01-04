import pytest
from unittest.mock import patch, ANY

from loft_temperature_feed_app.utils import ExternalApi

def test_task_id():
    assert ExternalApi.task_id == None

def test_websocket_uri():
    assert ExternalApi.websocket_uri == "ws://external_api:4000/graphql"

def test_websocket_payload():
    assert ExternalApi.websocket_payload == {
        "type": "start",
        "payload": {"query": "subscription { temperature }"}
    }

@pytest.mark.asyncio
async def test_save_temperature():
    mock_target = "loft_temperature_feed_app.utils.Temperature.objects.create"
    with patch(mock_target) as mock_create:
        await ExternalApi.save_temperature(temperature=20.0)
        mock_create.assert_called_once_with(value=20.0, timestamp=ANY)
 