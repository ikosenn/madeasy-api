from django.db import models
from django.contrib.postgres.fields import ArrayField

from mptt.models import MPTTModel, TreeForeignKey

from madeasy.common.models import AbstractBase


class CityLookup(AbstractBase):
    """
    Cities and their iata codes. This helps during lookup for cities
    to get flight details
    """
    city = models.CharField(max_length=255)
    city_code = models.CharField(max_length=3)
    airport_code = models.CharField(max_length=3)

    def __str__(self):
        return self.city


class Airport(AbstractBase):
    """
    This detail the location of an airport. This is either
    where the aircraft's destination or origin location
    """
    airport_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    iata = models.CharField(
        max_length=3, null=True, blank=True,
        help_text=(
            'FAA for airports located in Country'
            ' United States of America 3-letter IATA code, '
            'for all other airports.'))
    icao = models.CharField(max_length=4, null=True, blank=True)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    altitude = models.FloatField()
    timezone_offset = models.FloatField()
    dst = models.CharField(max_length=1)
    timezone = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.airport_name


class Airline(AbstractBase):
    """
    These is an airline to which a plane can belong to such as
    KLM
    """
    airline_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True, blank=True)
    iata = models.CharField(max_length=2, null=True, blank=True)
    icao = models.CharField(max_length=3, null=True, blank=True)
    callsign = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    active = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return self.airline_name


class Trip(AbstractBase):
    """
    Details about a trip from a departure airport to an arival airport
    """
    origin = models.ForeignKey(CityLookup, related_name='trip_origin')
    destination = models.ForeignKey(
        CityLookup, related_name='trip_destination')
    price = models.CharField(max_length=50, default='KES0')

    def __str__(self):
        return "-".join([
            self.origin.city, self.destination.city
        ])


class Flight(AbstractBase):
    """
    A trip can have one or more flights based on how many segments
    constitute a trip.
    """

    airline = models.ForeignKey(Airline)
    trip = models.ForeignKey(Trip)
    flight_number = models.CharField(max_length=50)
    origin = models.ForeignKey(Airport, related_name='flight_origin')
    destination = models.ForeignKey(Airport, related_name='flight_destination')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return self.flight_number


class Route(AbstractBase):
    """
    Stores details about a particular route
    """

    airline = models.ForeignKey(Airline)
    source_airport = models.ForeignKey(Airport, related_name='source_airport')
    destination_airport = models.ForeignKey(
        Airport, related_name='destination_airport')
    codeshare = models.CharField(
        max_length=1, null=True,
        help_text=('A flight is a codeshare if not operated by Airline,'
                   'but another carrier'))
    equipment = ArrayField(
        models.CharField(
            max_length=3, help_text='3-letter codes for plane type'))
    stops = models.IntegerField()

    def __str__(self):
        return self.airline_name + ' ' + \
            self.source_airport.airport_name + \
            "->" + self.destination_airport.airport_name


class RouteTree(MPTTModel, AbstractBase):
    """
    This are the allowed routes by an airline it uses MPTT
    """
    airline = models.ForeignKey(Airline)
    airport = models.ForeignKey(Airport)
    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children', db_index=True)

    def __str__(self):
        return self.airline.airline_name + ' ' + self.airport.airport_name + \
            "(" + self.airport.iata + ")"
