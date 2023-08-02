from django.urls import path, include
from apps.users.views import UserProfileViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', UserProfileViewSet, basename='user'),

urlpatterns = [
    path('', include(router.urls)),

]

