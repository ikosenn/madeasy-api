from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import (
    Airline,
    Airplane,
    TravelClass,
    Flight,
    TravelClassSeatCapacity,
)

from .serializers import (
    AirlineSerializer,
    AirplaneSerializer,
    TravelClassSerializer,
    FlightSerializer,
    TravelClassSeatCapacitySerializer,
)


class AirlineListView(ListCreateAPIView):

    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer


class AirlineDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    lookup_field = 'pk'


class AirplaneListView(ListCreateAPIView):

    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


class AirplaneDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    lookup_field = 'pk'


class TravelClassListView(ListCreateAPIView):

    queryset = TravelClass.objects.all()
    serializer_class = TravelClassSerializer


class TravelClassDetailView(RetrieveUpdateDestroyAPIView):

    queryset = TravelClass.objects.all()
    serializer_class = TravelClassSerializer
    lookup_field = 'pk'


class FlightListView(ListCreateAPIView):

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    lookup_field = 'pk'


class TravelClassSeatCapacityListView(ListCreateAPIView):

    queryset = TravelClassSeatCapacity.objects.all()
    serializer_class = TravelClassSeatCapacitySerializer


class TravelClassSeatCapacityDetailView(RetrieveUpdateDestroyAPIView):

    queryset = TravelClassSeatCapacity.objects.all()
    serializer_class = TravelClassSeatCapacitySerializer
    lookup_field = 'pk'
