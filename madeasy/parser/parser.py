def move_command_processor(move_cmd):
    """
    This is object processor for Book Command instances.
    It implements a default departure country to the current country
    the user is located in
    """
    pass


class Parser(object):
    def interpret(self, model):
        # model is an instance of Program
        for c in model.commands:
            if c.__class__.__name__ == "BookCommand":
                print("Book command invoked")
                print("To country {}, from country {}"
                      .format(c.country_arrive, c.country_departure))
                print("Departure date {}, return date {}"
                      .format(c.date_leave, c.date_return))
