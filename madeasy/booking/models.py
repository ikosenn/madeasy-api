from django.db import models
from django.conf import settings

from madeasy.airline.models import (
    TravelClass,
    Flight
)


BOOKING_STATUS = ()


class TicketType(models.Model):
    """
    What a passenger uses to identify their booking
    and succesful payment
    """

    ticket_code = models.CharField(max_length=100)


class BookingStatus(models.Model):
    """
    The status that a particular booking can belong to
    """

    name = models.CharField(max_length=50, choices=BOOKING_STATUS)


class Booking(models.Model):
    """
    Stores the booking of a particular class
    """

    booking_date = models.DateTimeField()
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL)
    booking_status = models.ForeignKey(BookingStatus)
    ticket_type = models.ForeignKey(TicketType)
    flight = models.ForeignKey(Flight)
    travel_class = models.ForeignKey(TravelClass)