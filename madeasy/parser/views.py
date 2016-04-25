from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from textx.exceptions import TextXSyntaxError
from madeasy.parser import parser_mm
from madeasy.parser.parser import Parser
from madeasy.parser.serializers import (
    ParserSerializer,
    ParserResultsSerializer
)
from madeasy.parser.models import ParserResults


class ParserView(APIView):
    """
    Provides post functionality that interacts with the parser
    """

    def post(self, request, *args, **kwargs):
        serializer = ParserSerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.data.get('query')
            try:
                parser_model = parser_mm.model_from_str(query)
                parser_obj = Parser()
                parser_obj.interpret(parser_model)
                if parser_obj.success_data:
                    return Response(
                        parser_obj.success_data, status=status.HTTP_200_OK)
            except TextXSyntaxError:
                error = {
                    'detail': ('The query was not properly formatted.'
                               ' Kindly see below for examples')}

        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class ParserResultsViewSet(viewsets.ModelViewSet):

    queryset = ParserResults.objects.all()
    serializer_class = ParserResultsSerializer
