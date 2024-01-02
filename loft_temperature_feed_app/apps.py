from django.apps import AppConfig

class LoftTemperatureFeedAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loft_temperature_feed_app'

    def ready(self):
        from loft_temperature_feed_app.tasks import ingest_temperatures
        ingest_temperatures.delay()
        pass
