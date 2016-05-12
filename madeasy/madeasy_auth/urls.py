from django.conf.urls import url
from rest_framework import routers

from .views import (
    UserViewSet,
    UserProfileViewSet,
    OauthApplicationViewSet,
    CreateUserView,
)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'applications', OauthApplicationViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^create_user/$', CreateUserView.as_view(), name="create_user"),
]
