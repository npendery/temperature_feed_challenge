import graphene
from graphene_django import DjangoObjectType

from loft_temperature_feed_app.models import Temperature
from loft_temperature_feed_app.utils import ExternalApi
from loft_temperature_feed_app.tasks import ingest_temperatures


class TemperatureType(DjangoObjectType):
    min = graphene.Float()
    max = graphene.Float()

    class Meta:
        model = Temperature
        fields = ("id", "value", "timestamp")


class ToggleFeedStatusInput(graphene.InputObjectType):
    status = graphene.String(required=True)


class ToggleFeedStatus(graphene.Mutation):
    class Arguments:
        input = ToggleFeedStatusInput(required=True)

    status = graphene.String()

    def mutate(root, info, input):
        if input.status == "on" and not ExternalApi.task_id:
            task = ingest_temperatures.delay()
            ExternalApi.task_id = task.id
        elif input.status == "off" and ExternalApi.task_id:
            ingest_temperatures.AsyncResult(task_id=ExternalApi.task_id).revoke(
                terminate=True
            )

        return ToggleFeedStatus(status=input.status)


class Mutations(graphene.ObjectType):
    toggle_feed = ToggleFeedStatus.Field()


class Query(graphene.ObjectType):
    status = graphene.String()

    all_temperatures = graphene.List(TemperatureType)

    def resolve_all_temperatures(root, info):
        return Temperature.objects.all()

    current_temperature = graphene.Field(TemperatureType, id=graphene.Int())

    def resolve_current_temperature(root, info):
        return Temperature.objects.latest("timestamp")

    temperature_statistics = graphene.Field(
        TemperatureType, before=graphene.DateTime(), after=graphene.DateTime()
    )

    def resolve_temperature_statistics(root, info, before=None, after=None, **kwargs):
        filtered_temperatures = Temperature.objects

        if after:
            filtered_temperatures = filtered_temperatures.filter(timestamp__gte=after)

        if before:
            filtered_temperatures = filtered_temperatures.filter(timestamp__lte=before)

        if filtered_temperatures.count() == 0:
            return None

        max_temperature = filtered_temperatures.order_by("-value").first()
        min_temperature = filtered_temperatures.order_by("value").first()

        return TemperatureType(min=min_temperature.value, max=max_temperature.value)


schema = graphene.Schema(query=Query, mutation=Mutations)
