from django.conf.urls import url

from .views import (
    TicketTypeListView,
    TicketTypeDetailView,
    BookingStatusListView,
    BookingStatusDetailView,
    BookingListView,
    BookingDetailView,
)


urlpatterns = [
    url(r'^ticket_types/$',
        TicketTypeListView.as_view(), name='ticket_types_list'),
    url(r'^ticket_types/(?P<pk>[0-9]+)/$',
        TicketTypeDetailView.as_view(), name='ticket_types_detail'),

    url(r'^booking_status/$',
        BookingStatusListView.as_view(), name='booking_status_list'),
    url(r'^booking_status/(?P<pk>[0-9]+)/$',
        BookingStatusDetailView.as_view(), name='booking_status_detail'),

    url(r'^bookings/$',
        BookingListView.as_view(), name='bookings_list'),
    url(r'^bookings/(?P<pk>[0-9]+)/$',
        BookingDetailView.as_view(), name='bookings_detail'),
]
