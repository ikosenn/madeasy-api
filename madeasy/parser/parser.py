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
        else:
            self.errors = serializer.errors

    def _search_book_command(self):
        """
        Search qpx for details regarding a flight
        """
        destination_airports = CityLookup.objects.filter(
            Q(city_code=self.country_arrive) | Q(city=self.country_arrive) |
            Q(airport_code=self.country_arrive))
        source_airports = CityLookup.objects.filter(
            Q(city_code=self.country_departure) |
            Q(city=self.country_departure) |
            Q(airport_code=self.country_departure))

        if destination_airports.exists() and source_airports.exists():
            payload = copy.deepcopy(QPX_REQUEST_PAYLOAD)
            temp = {
                "kind": "qpxexpress#sliceInput",
                "origin": source_airports[0].city_code,
                "destination": destination_airports[0].city_code,
                "date": self.date_departure,
            }
            payload['request']['slice'].append(temp)
            res = get_flight_details(
                payload, source_airports[0].city, destination_airports[0].city,
                source_airports[0].id, destination_airports[0].id)
            self.success_data = res
        else:
            raise ValidationError({
                'city': _("The departure or the arrival destinations are wrong"
                          ". Kindly check the spelling. We have strict "
                          "check and it must much an exact city")})


class Parser(Book):
    def __init__(self):
        self.errors = None

    def interpret(self, model):
        # model is an instance of Program
        for c in model.commands:
            if c.__class__.__name__ == "BookCommand":
                parsed_vars = {
                    'country_arrive': c.country_arrive,
                    'country_departure': c.country_departure,
                    'date_departure': convert_to_iso_date(c.date_leave),
                }

                # add date if its provided
                if c.date_return:
                    date_return = convert_to_iso_date(c.date_return)
                    parsed_vars['date_return'] = date_return
                # validate the data
                self._validate_book_command(parsed_vars)
                if self.errors:
                    raise ValidationError(self.errors)
                self._search_book_command()
