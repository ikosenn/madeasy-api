from django.conf.urls import url

from .views import (
    AirlineListView,
    AirlineDetailView,
    AirplaneListView,
    AirplaneDetailView,
    TravelClassListView,
    TravelClassDetailView,
    FlightListView,
    FlightDetailView,
    TravelClassSeatCapacityListView,
    TravelClassSeatCapacityDetailView,
)


urlpatterns = [
    url(r'^airlines/',
        AirlineListView.as_view(), name='airlines_list'),
    url(r'^airlines/(?P<pk>[0-9]+)$',
        AirlineDetailView.as_view(), name='airlines_detail'),

    url(r'^airplanes',
        AirplaneListView.as_view(), name='airplanes_list'),
    url(r'^airplanes/(?P<pk>[0-9]+)$',
        AirplaneDetailView.as_view(), name='airplanes_detail'),

    url(r'^travel_classes/',
        TravelClassListView.as_view(), name='travel_classes_list'),
    url(r'^travel_classes/(?P<pk>[0-9]+)$',
        TravelClassDetailView.as_view(), name='travel_classes_detail'),

    url(r'^flights/',
        FlightListView.as_view(), name='flights_list'),
    url(r'^flights/(?P<pk>[0-9]+)$',
        FlightDetailView.as_view(), name='flights_detail'),

    url(r'^travel_seat_capacities/',
        TravelClassSeatCapacityListView.as_view(),
        name='travel_seat_capacities_list'),
    url(r'^travel_seat_capacities/(?P<pk>[0-9]+)$',
        TravelClassSeatCapacityDetailView.as_view(),
        name='travel_seat_capacities_detail'),
]
