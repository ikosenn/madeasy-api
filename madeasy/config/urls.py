"""madeasy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

from madeasy.madeasy_auth.views import MeView

urlpatterns = [
    url(r'^o/',
        include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^accounts/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/',
        include('madeasy.madeasy_auth.urls', namespace='auth')),
    url(r'^api/booking/',
        include('madeasy.booking.urls', namespace='booking')),
    url(r'^api/payment/',
        include('madeasy.payment.urls', namespace='payment')),
    url(r'^api/airline/',
        include('madeasy.airline.urls', namespace='airline')),

    url(r'^api/parser/', include('madeasy.parser.urls', namespace='parser')),
    url(r'^me/$', MeView.as_view(), name='me'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
