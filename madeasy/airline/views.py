from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework import status

from madeasy.booking.models import Booking
from .models import (
    CityLookup,
    Airport,
    Airline,
    Flight,
    Route,
    RouteTree,
    Trip,
)

from .serializers import (
    AirportSerializer,
    AirlineSerializer,
    FlightSerializer,
    RouteSerializer,
    RouteTreeSerializer,
    CityLookupSerializer,
    TripSerializer,
)


class AirportViewSet(viewsets.ModelViewSet):

    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirlineViewSet(viewsets.ModelViewSet):

    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer


class FlightViewSet(viewsets.ModelViewSet):

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class RouteViewSet(viewsets.ModelViewSet):

    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteTreeViewSet(viewsets.ModelViewSet):

    queryset = RouteTree.objects.all()
    serializer_class = RouteTreeSerializer


class CityLookupViewSet(viewsets.ModelViewSet):

    queryset = CityLookup.objects.all()
    serializer_class = CityLookupSerializer


class TripViewSet(viewsets.ModelViewSet):

    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    @list_route(methods=['post'])
    def create_trip(self, request):
        user = request.user
        flight_details = request.data.get('flight_details', None)
        if flight_details:
            origin_id = flight_details.get('origin_id')
            destination_id = flight_details.get('destination_id')
            leg = flight_details.get('leg')
            segments = leg.get('segments')
            price = leg.get('price')
            origin = CityLookup.objects.get(id=origin_id)
            dest = CityLookup.objects.get(id=destination_id)
            trip = Trip.objects.create(
                origin=origin, destination=dest, price=price)
            for segment in segments:
                flight_number = segment['flight_number']
                start_time = segment['start_time']
                stop_time = segment['stop_time']
                start_airport = Airport.objects.get(
                    iata=segment['start_airport'])
                stop_airport = Airport.objects.get(
                    iata=segment['stop_airport'])
                airline = Airline.objects.get(iata=segment['airline'])

                flight = Flight.objects.create(
                    airline=airline, trip=trip, flight_number=flight_number,
                    origin=start_airport, destination=stop_airport,
                    departure_time=start_time, arrival_time=stop_time
                )
                Booking.objects.create(passenger=user, flight=flight)
                serializer = TripSerializer(trip)
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED)
        else:
            raise ValidationError({
                'flight_details': 'You must submit valid flight details'
            })
