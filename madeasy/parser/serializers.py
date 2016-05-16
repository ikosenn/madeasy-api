from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from rest_framework import serializers
from rest_framework.serializers import ValidationError

from madeasy.common.serializers import AuditFieldsMixin
from madeasy.parser.models import ParserResults


class ParserSerializer(serializers.Serializer):
    """
    A serializer that process the query provided by the front-end
    """

    query = serializers.CharField(max_length=255)


class ParserResultsSerializer(AuditFieldsMixin):

    class Meta:
        model = ParserResults
        read_only_fields = ('response_time', 'parser_time')


class BookCommandSerializer(serializers.Serializer):
    """
    Serializer that handles validations on the book command
    """
    country_arrive = serializers.CharField()
    country_departure = serializers.CharField()
    date_departure = serializers.DateField()
    date_return = serializers.DateField(required=False)
    price = serializers.FloatField(required=False, min_value=0)

    def validate(self, data):
        """
        Check that a ``date_departure`` is less than the ``date_return``
        """

        if data.get('date_return'):
            if data['date_return'] < data['date_departure']:
                raise ValidationError({
                    'date_return': _("The return date should greater than"
                                     " the departure date.")})
        return data

    def validate_date_departure(self, value):
        """
        Validate the the departure date is greater than todays date
        """

        if timezone.now().date() > value:
            raise ValidationError("The departure date should be greater "
                                  "than today's date.")
        return value

    def validate_date_return(self, value):
        """
        Validate the the departure date is greater than todays date
        """

        if timezone.now().date() > value:
            raise ValidationError("The return date should be greater "
                                  "than today's date.")
        return value
