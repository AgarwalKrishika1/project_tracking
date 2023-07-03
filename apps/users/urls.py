from django.urls import path, include
from apps.users.views import UserProfileModelView, CustomUserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserProfileModelView, basename='user'),
router.register(r'create user', CustomUserViewSet, basename='createuser')

urlpatterns = [
    path('', include(router.urls))
]
