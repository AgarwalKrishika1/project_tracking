from django.urls import path, include
from apps.comments import CommentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', CommentViewSet, basename=''),

urlpatterns = [
    path('', include(router.urls))
]
