from madeasy.parser.serializers import BookCommandSerializer
from madeasy.common.utility import convert_to_iso_date


def move_command_processor(move_cmd):
    """
    This is object processor for Book Command instances.
    It implements a default departure country to the current country
    the user is located in
    """
    pass


class Parser(object):
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
            self.date_departure = data.get('date_leave')
            self.date_return = data.get('date_return')
        else:
            self.errors = serializer.errors
