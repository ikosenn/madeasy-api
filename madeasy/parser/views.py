import datetime

from django.db.models import Avg
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import list_route


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
        start_time = datetime.datetime.now()
        serializer = ParserSerializer(data=request.data)
        parser_results = ParserResults()
        query_raw = request.data.get('query', '')
        parser_results.query_raw = query_raw
        parser_results.created_by = request.user
        parser_results.save()
        if serializer.is_valid():
            query = serializer.data.get('query')
            parser_results.query = query
            try:
                parser_model = parser_mm.model_from_str(query)
                parser_obj = Parser(request.user)
                parser_obj.interpret(parser_model)
                parser_results.command_executed = parser_obj.command_executed
                if parser_obj.success_data:
                    stop_time = datetime.datetime.now()
                    total_seconds = (stop_time - start_time).total_seconds()
                    parser_results.response_time = total_seconds
                    parser_results.is_correct = True
                    parser_results.save()
                    return Response(
                        parser_obj.success_data, status=status.HTTP_200_OK)
            except TextXSyntaxError:
                error = {
                    'detail': ('The query was not properly formatted.'
                               ' Kindly see below for examples')}
                parser_results.save()
                return Response(error, status=status.HTTP_400_BAD_REQUEST)
        parser_results.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParserResultsViewSet(viewsets.ModelViewSet):

    queryset = ParserResults.objects.all()
    serializer_class = ParserResultsSerializer

    @list_route(methods=['get'])
    def parser_correctness(self, request):
        pos = ParserResults.objects.filter(is_correct=True)
        neg = ParserResults.objects.filter(is_correct=False)

        parser_correctness = {
            "positive": pos.count(),
            "negative": neg.count()
        }
        return Response(parser_correctness, status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def parser_command_type(self, request):
        unknown = ParserResults.objects.filter(command_executed="Unkwown")
        book = ParserResults.objects.filter(command_executed="BookCommand")
        show = ParserResults.objects.filter(command_executed="ShowCommand")

        parser_correctness = {
            "unknown": unknown.count(),
            "book": book.count(),
            "show": show.count()
        }
        return Response(parser_correctness, status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def parser_numbers(self, request):
        today = ParserResults.objects.filter(
            created__gt=timezone.now().date())
        pos = ParserResults.objects.filter(is_correct=True)
        neg = ParserResults.objects.filter(is_correct=False)

        parser_correctness = {
            "today": today.count(),
            "positive": pos.count(),
            "negative": neg.count()
        }
        return Response(parser_correctness, status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def parser_response_day(self, request):
        response = ParserResults.objects.filter(is_correct=True).extra({
            'created': 'date(created)'
        }).values('created').annotate(average_res_time=Avg('response_time'))

        return Response(response, status=status.HTTP_200_OK)
