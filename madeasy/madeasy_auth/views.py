from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView
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


class MeView(RetrieveUpdateAPIView):

    queryset = None
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
