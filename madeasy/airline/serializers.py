from rest_framework import serializers


from .models import (
    Airline,
    Airplane,
    TravelClass,
    Flight,
    TravelClassSeatCapacity,
)


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane


class TravelClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelClass


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight


class TravelClassSeatCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelClassSeatCapacity
