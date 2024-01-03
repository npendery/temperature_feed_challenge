from celery import shared_task
import asyncio

@shared_task
def ingest_temperatures():
    from loft_temperature_feed_app.utils import ExternalApi
    asyncio.run(ExternalApi.ingest_temperatures())
