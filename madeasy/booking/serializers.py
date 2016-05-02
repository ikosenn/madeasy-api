from madeasy.common.serializers import AuditFieldsMixin

from madeasy.booking.models import Booking


class BookingSerializer(AuditFieldsMixin):
    class Meta:
        model = Booking
