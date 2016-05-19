from django.db import models
from madeasy.common.models import AbstractBase


class ParserResults(AbstractBase):
    """
    This model store the statistics of a particular
    """

    query = models.CharField(max_length=255)
    parser_time = models.FloatField(
        default=0.0,
        help_text='The time it takes the parser to understand the query')
    response_time = models.DecimalField(
        default=0.0,
        help_text='The time it takes from querying to fetching a result',
        decimal_places=3,
        max_digits=10)
    is_correct = models.BooleanField(default=False)
    command_executed = models.CharField(max_length=50, default="Unkwown")
