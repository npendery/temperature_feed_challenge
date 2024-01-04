from datetime import datetime
import websockets
import json
from loft_temperature_feed_app.models import Temperature
from asgiref.sync import sync_to_async

class ExternalApi:
    task_id = None
    websocket_uri = "ws://external_api:4000/graphql"
    websocket_payload = {
        "type": "start",
        "payload": {"query": "subscription { temperature }"}
    }

    async def ingest_temperatures():
        async with websockets.connect(ExternalApi.websocket_uri, subprotocols=["graphql-ws"]) as websocket:
            await websocket.send(json.dumps(ExternalApi.websocket_payload))
            while True:
                data = await websocket.recv()
                json_data = json.loads(data)
                temperature = json_data["payload"]["data"]["temperature"]
                await ExternalApi.save_temperature(temperature)

    @sync_to_async
    def save_temperature(self, temperature):
        Temperature.objects.create(value=temperature, timestamp=datetime.now())

