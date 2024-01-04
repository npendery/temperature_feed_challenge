from celery import shared_task
from loft_temperature_feed_app.utils import ExternalApi
import asyncio

@shared_task
def ingest_temperatures() -> None:
    asyncio.run(ExternalApi.ingest_temperatures())
