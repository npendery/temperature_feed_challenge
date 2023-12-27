import graphene
from graphene_django import DjangoObjectType

from loft_temperature_feed_app.models import Temperature

class TemperatureType(DjangoObjectType):
    class Meta:
        model = Temperature
        fields = ("id", "temperature", "timestamp")

class Query(graphene.ObjectType):
    all_temperatures = graphene.List(TemperatureType)

    def resolve_all_temperatures(root, info):
        return Temperature.objects.all()

schema = graphene.Schema(query=Query)