import pytest
from unittest.mock import patch, ANY

from loft_temperature_feed_app.utils import ExternalApi


def test_task_id():
    """
    The task_id should be None before the task is run.
    """
    assert ExternalApi.task_id == None


def test_websocket_uri():
    """
    The websocket_uri should be ws://external_api:4000/graphql.
    """
    assert ExternalApi.websocket_uri == "ws://external_api:4000/graphql"


def test_websocket_payload():
    """
    The websocket_payload should be:
    """
    assert ExternalApi.websocket_payload == {
        "type": "start",
        "payload": {"query": "subscription { temperature }"},
    }


@pytest.mark.asyncio
async def test_save_temperature():
    """
    The save_temperature method should create a new Temperature object.
    """
    mock_target = "loft_temperature_feed_app.utils.Temperature.objects.create"
    with patch(mock_target) as mock_create:
        await ExternalApi.save_temperature(temperature=20.0)
        mock_create.assert_called_once_with(value=20.0, timestamp=ANY)
