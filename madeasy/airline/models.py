from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from madeasy.common.models import AbstractBase


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
        return self.name


class Airplane(AbstractBase):
    """
    The actual aircraft
    """

    aircraft_type = models.CharField(max_length=255)
    airline = models.ForeignKey(Airline)

    def __str__(self):
        return self.aircraft_type


class TravelClass(AbstractBase):
    """
    The travel class of the seat
    """

    travel_class_code = models.CharField(max_length=50)
    travel_class_name = models.CharField(max_length=255)

    def __str__(self):
        return self.travel_class_name


class Flight(AbstractBase):
    """
    This are the details partaining to a single journey.
    e.g. Moving from JKIA to Amsterdam
    """

    airplane = models.ForeignKey(Airplane)
    flight_number = models.CharField(max_length=50)
    origin = models.ForeignKey(Airport, related_name='origin')
    destination = models.ForeignKey(Airport, related_name='destination')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    travel_class = models.ManyToManyField(
        TravelClass, through='TravelClassSeatCapacity')

    def __str__(self):
        return self.flight_number


class TravelClassSeatCapacity(AbstractBase):
    """
    Through table between a travel class and a flight
    """

    flight = models.ForeignKey(Flight)
    travel_class = models.ForeignKey(TravelClass)
    seat_capacity = models.IntegerField()
    seat_price = models.FloatField()

    def __str__(self):
        return self.seat_capacity


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
    equipment = models.CharField(
        max_length=3, help_text='3-letter codes for plane type')
    stops = models.IntegerField()


class RouteTree(MPTTModel, AbstractBase):
    """
    This are the allowed routes by an airline it uses MPTT
    """
    airline = models.ForeignKey(Airline)
    airport = models.ForeignKey(Airport)
    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children', db_index=True)
