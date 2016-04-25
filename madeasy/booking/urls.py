from rest_framework import routers

from .views import (
    TicketTypeViewSet,
    BookingStatusViewSet,
    BookingViewSet,
    FlightDetailsViewSet,
)


router = routers.DefaultRouter()
router.register(r'ticket_types', TicketTypeViewSet)
router.register(r'booking_status', BookingStatusViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'flight_details', FlightDetailsViewSet)

urlpatterns = router.urls
