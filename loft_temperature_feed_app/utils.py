from datetime import datetime
import websockets
import json
from loft_temperature_feed_app.models import Temperature
from asgiref.sync import sync_to_async

class ExternalApi:
    async def ingest_temperatures():
        uri = "ws://external_api:1000/graphql"
        start = {
            "type": "start",
            "payload": {"query": "subscription { temperature }"}
        }
        async with websockets.connect(uri, subprotocols=["graphql-ws"]) as websocket:
            await websocket.send(json.dumps(start))
            while True:
                data = await websocket.recv()
                json_data = json.loads(data)
                temperature = json_data["payload"]["data"]["temperature"]
                print(temperature)
                await ExternalApi.save_temperature(temperature)

    @sync_to_async
    def save_temperature(self, temperature):
        Temperature.objects.create(value=temperature, timestamp=datetime.now())

