from django.db import models


class Airline(models.Model):
    """
    These is an airline to which a plane can belong to such as
    KLM
    """
    name = models.CharField(max_length=255)


class Airplane(models.Model):
    """
    The actual aircraft
    """

    aircraft_type = models.CharField(max_length=255)
    airline = models.ForeignKey(Airline)


class TravelClass(models.Model):
    """
    The travel class of the seat
    """

    travel_class_code = models.CharField(max_length=50)


class Flight(models.Model):
    """
    This are the details partaining to a single journey.
    e.g. Moving from JKIA to Amsterdam
    """

    airplane = models.ForeignKey(Airplane)
    flight_number = models.CharField(max_length=50)
    destination = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    travel_class = models.ManyToManyField(
        TravelClass, through='TravelClassSeatCapacity')


class TravelClassSeatCapacity(models.Model):
    """
    Through table between a travel class and a flight
    """

    flight = models.ForeignKey(Flight)
    travel_class = models.ForeignKey(TravelClass)
    seat_capacity = models.IntegerField()
