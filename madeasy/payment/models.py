from django.db import models
from madeasy.booking.models import Booking


PAYMENT_TYPE = (
    ('M-PESA', 'MPESA'),
)


class Payment(models.Model):
    """
    Records the payment of a particular booking.
    Multiple payments can be made for each booking
    """
    booking = models.ForeignKey(Booking)
    payment_method = models.CharField(
        max_length=50, choices=PAYMENT_TYPE, default='MPESA')
    amount = models.FloatField(default=0)
