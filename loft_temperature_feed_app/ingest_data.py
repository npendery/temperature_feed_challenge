from loft_temperature_feed_app.utils import ExternalApi

import asyncio

print("Starting ingestion")

asyncio.run(ExternalApi.ingest_temperatures())
