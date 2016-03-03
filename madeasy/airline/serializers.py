from madeasy.common.serializers import AuditFieldsMixin

from madeasy.airline.models import (
    Airline,
    Airplane,
    TravelClass,
    Flight,
    TravelClassSeatCapacity,
    Airport,
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
