from rest_framework import routers

from .views import (
    AirportViewSet,
    AirlineViewSet,
    AirplaneViewSet,
    TravelClassViewSet,
    FlightViewSet,
    TravelClassSeatCapacityViewSet,
)


router = routers.DefaultRouter()
router.register(r'airports', AirportViewSet)
router.register(r'airlines', AirlineViewSet)
router.register(r'airplanes', AirplaneViewSet)
router.register(r'travel_classes', TravelClassViewSet)
router.register(r'flights', FlightViewSet)
router.register(
    r'travel_class_seat_capacities', TravelClassSeatCapacityViewSet)

urlpatterns = router.urls
