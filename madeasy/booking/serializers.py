from rest_framework import serializers


from .models import (
    TicketType,
    BookingStatus,
    Booking,
)


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType


class BookingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingStatus


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
