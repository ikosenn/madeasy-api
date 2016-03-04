from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

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
            print(query)
            parser_model = parser_mm.model_from_str(query)
            parser_obj = Parser()
            parser_obj.interpret(parser_model)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParserResultsViewSet(viewsets.ModelViewSet):

    queryset = ParserResults.objects.all()
    serializer_class = ParserResultsSerializer
