from django.urls import path, include
from apps.issues.views import IssueViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', IssueViewSet, basename='issues'),

urlpatterns = [
    path('', include(router.urls))
]
