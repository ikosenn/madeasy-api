from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

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


class UserListView(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


class UserProfileListView(ListCreateAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'pk'


class OauthApplicationListView(ListCreateAPIView):

    queryset = OauthApplication.objects.all()
    serializer_class = OauthApplicationSerializer


class OauthApplicationDetailView(RetrieveUpdateDestroyAPIView):

    queryset = OauthApplication.objects.all()
    serializer_class = OauthApplicationSerializer
    lookup_field = 'pk'
