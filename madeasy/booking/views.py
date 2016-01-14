from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

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


class TicketTypeListView(ListCreateAPIView):

    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer


class TicketTypeDetailView(RetrieveUpdateDestroyAPIView):

    queryset = TicketType.objects.all()
    serializer_class = TicketTypeSerializer
    lookup_field = 'pk'


class BookingStatusListView(ListCreateAPIView):

    queryset = BookingStatus.objects.all()
    serializer_class = BookingStatusSerializer


class BookingStatusDetailView(RetrieveUpdateDestroyAPIView):

    queryset = BookingStatus.objects.all()
    serializer_class = BookingStatusSerializer
    lookup_field = 'pk'


class BookingListView(ListCreateAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = 'pk'
