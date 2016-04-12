from rest_framework import viewsets

from .models import (
    TicketType,
    BookingStatus,
    Booking,
    FlightDetails,
)

from .serializers import (
    TicketTypeSerializer,
    BookingStatusSerializer,
    BookingSerializer,
    FlightDetailsSerializer
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


class FlightDetailsViewSet(viewsets.ModelViewSet):

    queryset = FlightDetails.objects.all()
    serializer_class = FlightDetailsSerializer
