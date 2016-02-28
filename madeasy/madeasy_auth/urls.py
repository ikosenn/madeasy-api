from rest_framework import routers

from .views import (
    UserViewSet,
    UserProfileViewSet,
    OauthApplicationViewSet,
)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'applications', OauthApplicationViewSet)

urlpatterns = router.urls
