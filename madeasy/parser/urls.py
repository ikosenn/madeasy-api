from django.conf.urls import url
from rest_framework import routers
from madeasy.parser.views import (
    ParserView,
    ParserResultsViewSet
)


urlpatterns = [
    url(r'^parse_query/$', ParserView.as_view(), name='parse_query')

]

router = routers.DefaultRouter()
router.register(r'parser_results', ParserResultsViewSet)
urlpatterns += router.urls
