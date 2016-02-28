from rest_framework import viewsets

from .models import (
    User,
    UserProfile,
    OauthApplication,
)

from .serializers import (
    UserSerializer,
    UserProfileSerializer,
    OauthApplicationSerializer,
)


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class OauthApplicationViewSet(viewsets.ModelViewSet):

    queryset = OauthApplication.objects.all()
    serializer_class = OauthApplicationSerializer
