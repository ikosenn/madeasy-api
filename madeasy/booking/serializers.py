from madeasy.common.serializers import AuditFieldsMixin

from madeasy.booking.models import (
    TicketType,
    BookingStatus,
    Booking,
)


class TicketTypeSerializer(AuditFieldsMixin):
    class Meta:
        model = TicketType


class BookingStatusSerializer(AuditFieldsMixin):
    class Meta:
        model = BookingStatus


class BookingSerializer(AuditFieldsMixin):
    class Meta:
        model = Booking
