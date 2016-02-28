from rest_framework import viewsets

from .models import (
    TicketType,
    BookingStatus,
    Booking,
)

from .serializers import (
    TicketTypeSerializer,
    BookingStatusSerializer,
    BookingSerializer,
)


class TicketTypeViewSet(viewsets.ModelViewSet):

    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer


class BookingStatusViewSet(viewsets.ModelViewSet):

    queryset = BookingStatus.objects.all()
    serializer_class = BookingStatusSerializer


class BookingViewSet(viewsets.ModelViewSet):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
