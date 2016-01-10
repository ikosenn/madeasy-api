from rest_framework import serializers


from .models import (
    User,
    UserProfile,
    EmrOauthApplication,
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile


class OauthApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OauthApplication
