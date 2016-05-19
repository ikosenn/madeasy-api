import copy
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from rest_framework.serializers import ValidationError
from madeasy.parser.serializers import BookCommandSerializer
from madeasy.common.utility import convert_to_iso_date

from madeasy.parser.qpx import QPX_REQUEST_PAYLOAD, get_flight_details
from madeasy.airline.models import CityLookup


def move_command_processor(move_cmd):
    """
    This is object processor for Book Command instances.
    It implements a default departure country to the current country
    the user is located in
    """
    pass


class Book(object):
    """
    Validation, search functions of the BookCommand
    """

    def _validate_book_command(self, parsed_vars):
        """
        Method that validates book type of commands. It does so by using the
        ``BookCommandSerializer``
        """

        serializer = BookCommandSerializer(data=parsed_vars)
        if serializer.is_valid():
            data = serializer.data
            self.country_arrive = data.get('country_arrive')
            self.country_departure = data.get('country_departure')
            self.date_departure = data.get('date_departure')
            self.date_return = data.get('date_return')
            self.price = data.get('price')
            self.adult_count = data.get('adult_count')
        else:
            self.errors = serializer.errors

    def _search_book_command(self):
        """
        Search qpx for details regarding a flight
        """
        destination_airports = CityLookup.objects.filter(
            Q(city_code__icontains=self.country_arrive) |
            Q(city__icontains=self.country_arrive) |
            Q(airport_code__icontains=self.country_arrive))
        source_airports = CityLookup.objects.filter(
            Q(city_code__icontains=self.country_departure) |
            Q(city__icontains=self.country_departure) |
            Q(airport_code__icontains=self.country_departure))

        if destination_airports.exists() and source_airports.exists():
            payload = copy.deepcopy(QPX_REQUEST_PAYLOAD)
            temp = {
                "kind": "qpxexpress#sliceInput",
                "origin": source_airports[0].city_code,
                "destination": destination_airports[0].city_code,
                "date": self.date_departure,
            }
            payload['request']['slice'].append(temp)
            if self.date_return:
                temp = {
                    "kind": "qpxexpress#sliceInput",
                    "destination": source_airports[0].city_code,
                    "origin": destination_airports[0].city_code,
                    "date": self.date_return,
                }
                payload['request']['slice'].append(temp)
            if self.price:
                payload['request']['maxPrice'] = 'USD' + str(self.price)

            if self.adult_count:
                payload['request']['passengers']['adultCount'] = self.adult_count  # noqa
            res = get_flight_details(
                payload, source_airports[0].city, destination_airports[0].city,
                source_airports[0].id, destination_airports[0].id)
            self.success_data = res
        else:
            raise ValidationError({
                'city': _("The departure or the arrival destinations are wrong"
                          ". Kindly check the spelling. We have strict "
                          "check and it must much an exact city")})


class ShowBooked(object):
    """
    Executed to retrieve all the booked fights of a particular user
    """

    def _get_booked_flights(self):
        """
        Search qpx for details regarding a flight
        """

        results = {"command_type": "my_flights", "results": []}
        booked = self.user.my_flights
        if booked:
            for book in booked:
                trip = book.trip
                temp = {
                    "origin": trip.origin.city,
                    "destination": trip.destination.city,
                    "price": trip.price
                }
                segments = []
                for flight in trip.flight_set.all():
                    temp_leg = {
                        "stop_time": flight.arrival_time,
                        "start_time": flight.departure_time,
                        "start_airport": flight.origin.iata,
                        "stop_airport": flight.destination.iata,
                        "airline": flight.airline.iata
                    }
                    segments.append(temp_leg)
                temp["segments"] = segments
                results["results"].append(temp)
        self.success_data = results


class Parser(Book, ShowBooked):
    def __init__(self, user):
        self.errors = None
        self.command_executed = None
        self.user = user

    def interpret(self, model):
        # model is an instance of Program
        for c in model.commands:
            if c.__class__.__name__ == "BookCommand":
                self.command_executed = "BookCommand"
                parsed_vars = {
                    'country_arrive': c.country_arrive,
                    'country_departure': c.country_departure,
                    'date_departure': convert_to_iso_date(c.date_departure),
                }

                # add date if its provided
                if c.date_return:
                    date_return = convert_to_iso_date(c.date_return)
                    parsed_vars['date_return'] = date_return
                # add price if its provided
                if c.price:
                    parsed_vars['price'] = c.price
                # add adult count
                if c.adult_count:
                    parsed_vars['adult_count'] = c.adult_count
                # validate the data
                self._validate_book_command(parsed_vars)
                if self.errors:
                    raise ValidationError(self.errors)
                self._search_book_command()
            elif c.__class__.__name__ == "ShowCommand":
                self.command_executed = "ShowCommand"
                self._get_booked_flights()
