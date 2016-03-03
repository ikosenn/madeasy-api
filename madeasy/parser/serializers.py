from rest_framework import serializers

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
