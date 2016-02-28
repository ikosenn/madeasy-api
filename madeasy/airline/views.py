from rest_framework import viewsets

from .models import (
    Airline,
    Airplane,
    TravelClass,
    Flight,
    TravelClassSeatCapacity,
    Airport
)

from .serializers import (
    AirportSerializer,
    AirlineSerializer,
    AirplaneSerializer,
    TravelClassSerializer,
    FlightSerializer,
    TravelClassSeatCapacitySerializer,
)


class AirportViewSet(viewsets.ModelViewSet):

    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirlineViewSet(viewsets.ModelViewSet):

    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer


class AirplaneViewSet(viewsets.ModelViewSet):

    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


class TravelClassViewSet(viewsets.ModelViewSet):

    queryset = TravelClass.objects.all()
    serializer_class = TravelClassSerializer


class FlightViewSet(viewsets.ModelViewSet):

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class TravelClassSeatCapacityViewSet(viewsets.ModelViewSet):

    queryset = TravelClassSeatCapacity.objects.all()
    serializer_class = TravelClassSeatCapacitySerializer
