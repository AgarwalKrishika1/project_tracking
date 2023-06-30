from django.urls import path, include
from apps.users.views import UserProfileModelView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserProfileModelView, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
