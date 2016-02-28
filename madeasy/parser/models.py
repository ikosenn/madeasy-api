from django.db import models


class ParserResults(models.Model):
    """
    This model store the statistics of a particular
    """

    query = models.CharField(max_length=255)
    parser_time = models.FloatField(
        default=0.0,
        help_text='The time it takes the parser to understand the query')
    response_time = models.FloatField(
        default=0.0,
        help_text='The time it takes from querying to fetching a result')
    is_correct = models.BooleanField(default=True)
