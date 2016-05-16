from django.db import models
from django.utils import timezone
from django.conf import settings

from madeasy.airline.models import Trip

from madeasy.common.models import AbstractBase

BOOKING_STATUS = (
    ('CONFIRMED', 'CONFIRMED'),
    ('PENDING', 'PENDING')
)


class Booking(AbstractBase):
    """
    Stores the booking of a particular class
    """

    booking_date = models.DateTimeField(default=timezone.now)
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL)
    booking_status = models.CharField(
        max_length=50, choices=BOOKING_STATUS, default='PENDING')
    trip = models.ForeignKey(Trip)

    def __str__(self):
        return " - ".join([
            self.flight.flight_number, self.booking_status.name
        ])
