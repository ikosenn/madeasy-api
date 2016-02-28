from rest_framework import routers

from .views import (
    TicketTypeViewSet,
    BookingStatusViewSet,
    BookingViewSet,
)


router = routers.DefaultRouter()
router.register(r'ticket_types', TicketTypeViewSet)
router.register(r'booking_status', BookingStatusViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = router.urls
