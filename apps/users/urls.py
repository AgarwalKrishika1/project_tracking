from django.urls import path, include

from apps.users import views
from apps.users.views import UserProfileModelView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('', UserProfileModelView, basename='user'),

urlpatterns = [
    path('', include(router.urls)),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
#
# urlpatterns = router.urls
