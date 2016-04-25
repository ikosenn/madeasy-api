from rest_framework import viewsets

from .models import (
    Airline,
    Airplane,
    TravelClass,
    Flight,
    TravelClassSeatCapacity,
    Airport,
    Route,
    RouteTree,
    CityLookup,
)

from .serializers import (
    AirportSerializer,
    AirlineSerializer,
    AirplaneSerializer,
    TravelClassSerializer,
    FlightSerializer,
    TravelClassSeatCapacitySerializer,
    RouteSerializer,
    RouteTreeSerializer,
    CityLookupSerializer
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


class RouteViewSet(viewsets.ModelViewSet):

    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteTreeViewSet(viewsets.ModelViewSet):

    queryset = RouteTree.objects.all()
    serializer_class = RouteTreeSerializer


class TravelClassSeatCapacityViewSet(viewsets.ModelViewSet):

    queryset = TravelClassSeatCapacity.objects.all()
    serializer_class = TravelClassSeatCapacitySerializer


class CityLookupViewSet(viewsets.ModelViewSet):

    queryset = CityLookup.objects.all()
    serializer_class = CityLookupSerializer
