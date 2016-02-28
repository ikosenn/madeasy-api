from django.db import models


class Airport(models.Model):
    """
    This detail the location of an airport. This is either
    where the aircraft's destination or origin location
    """
    airport_name = models.CharField(max_length=255)
    airport_code = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.airport_name


class Airline(models.Model):
    """
    These is an airline to which a plane can belong to such as
    KLM
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Airplane(models.Model):
    """
    The actual aircraft
    """

    aircraft_type = models.CharField(max_length=255)
    airline = models.ForeignKey(Airline)

    def __str__(self):
        return self.aircraft_type


class TravelClass(models.Model):
    """
    The travel class of the seat
    """

    travel_class_code = models.CharField(max_length=50)
    travel_class_name = models.CharField(max_length=255)

    def __str__(self):
        return self.travel_class_name


class Flight(models.Model):
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


class TravelClassSeatCapacity(models.Model):
    """
    Through table between a travel class and a flight
    """

    flight = models.ForeignKey(Flight)
    travel_class = models.ForeignKey(TravelClass)
    seat_capacity = models.IntegerField()
    seat_price = models.FloatField()

    def __str__(self):
        return self.seat_capacity
