from django.db import models
from django.conf import settings

from madeasy.airline.models import (
    TravelClass,
    Flight,
)


BOOKING_STATUS = (
    ('CONFIRMED', 'CONFIRMED'),
    ('PENDING', 'PENDING')
)


class TicketType(models.Model):
    """
    What a passenger uses to identify their booking
    and succesful payment
    """

    ticket_code = models.CharField(max_length=100)

    def __str__(self):
        return self.ticket_code


class BookingStatus(models.Model):
    """
    The status that a particular booking can belong to
    """

    name = models.CharField(max_length=50, choices=BOOKING_STATUS)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return " - ".join([self.fligt.flight_number, self.booking_status.name])
