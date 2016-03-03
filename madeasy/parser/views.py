from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

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
            serializer.save()
            # return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParserResultsViewSet(viewsets.ModelViewSet):

    queryset = ParserResults.objects.all()
    serializer_class = ParserResultsSerializer
