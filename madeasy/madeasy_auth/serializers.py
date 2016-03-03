from madeasy.common.serializers import AuditFieldsMixin
from madeasy.madeasy_auth.models import (
    User,
    UserProfile,
    OauthApplication,
)


class UserSerializer(AuditFieldsMixin):
    class Meta:
        model = User


class UserProfileSerializer(AuditFieldsMixin):
    class Meta:
        model = UserProfile


class OauthApplicationSerializer(AuditFieldsMixin):
    class Meta:
        model = OauthApplication
