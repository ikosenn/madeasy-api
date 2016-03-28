from madeasy.common.serializers import AuditFieldsMixin

from madeasy.airline.models import (
    Airline,
    Airplane,
    TravelClass,
    Flight,
    TravelClassSeatCapacity,
    Airport,
    Route,
    RouteTree
)


class AirportSerializer(AuditFieldsMixin):
    class Meta:
        model = Airport


class AirlineSerializer(AuditFieldsMixin):
    class Meta:
        model = Airline


class AirplaneSerializer(AuditFieldsMixin):
    class Meta:
        model = Airplane


class TravelClassSerializer(AuditFieldsMixin):
    class Meta:
        model = TravelClass


class FlightSerializer(AuditFieldsMixin):
    class Meta:
        model = Flight


class TravelClassSeatCapacitySerializer(AuditFieldsMixin):
    class Meta:
        model = TravelClassSeatCapacity


class RouteSerializer(AuditFieldsMixin):
    class Meta:
        model = Route


class RouteTreeSerializer(AuditFieldsMixin):
    class Meta:
        model = RouteTree
