from madeasy.common.serializers import AuditFieldsMixin

from madeasy.airline.models import (
    CityLookup,
    Airport,
    Airline,
    Flight,
    Route,
    RouteTree,
    Trip,
)


class AirportSerializer(AuditFieldsMixin):
    class Meta:
        model = Airport


class AirlineSerializer(AuditFieldsMixin):
    class Meta:
        model = Airline


class FlightSerializer(AuditFieldsMixin):
    class Meta:
        model = Flight


class RouteSerializer(AuditFieldsMixin):
    class Meta:
        model = Route


class RouteTreeSerializer(AuditFieldsMixin):
    class Meta:
        model = RouteTree


class CityLookupSerializer(AuditFieldsMixin):
    class Meta:
        model = CityLookup


class TripSerializer(AuditFieldsMixin):
    class Meta:
        model = Trip
