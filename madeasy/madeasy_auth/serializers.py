from madeasy.common.serializers import AuditFieldsMixin
from madeasy.madeasy_auth.models import (
    User,
    UserProfile,
    OauthApplication,
)


class UserSerializer(AuditFieldsMixin):
    class Meta:
        model = User
        read_only_fields = ('last_login',)

    def create(self, validated_data):
        """
        Overide the create method to allow for the creation of new
        user using `create user` method
        """

        return User.objects.create_user(**validated_data)


class UserProfileSerializer(AuditFieldsMixin):
    class Meta:
        model = UserProfile


class OauthApplicationSerializer(AuditFieldsMixin):
    class Meta:
        model = OauthApplication
