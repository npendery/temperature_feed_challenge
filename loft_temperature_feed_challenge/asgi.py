"""
ASGI config for loft_temperature_feed_challenge project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import path

from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

from loft_temperature_feed_challenge.graphql_subscription_consumer import MyGraphqlWsConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loft_temperature_feed_challenge.settings')

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': URLRouter([
        path("graphql/", MyGraphqlWsConsumer.as_asgi()),
    ])
})
