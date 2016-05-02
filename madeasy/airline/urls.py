from rest_framework import routers

from .views import (
    AirportViewSet,
    AirlineViewSet,
    FlightViewSet,
    RouteViewSet,
    RouteTreeViewSet,
    CityLookupViewSet,
    TripViewSet,
)


router = routers.DefaultRouter()
router.register(r'airports', AirportViewSet)
router.register(r'airlines', AirlineViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'route_trees', RouteTreeViewSet)
router.register(r'city_lookup', CityLookupViewSet)
router.register(r'trips', TripViewSet)

urlpatterns = router.urls
