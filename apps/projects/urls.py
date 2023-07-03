from django.urls import path, include
from apps.projects.views import ClientViewSet, ProjectsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet, basename='clients'),
router.register(r'projects', ProjectsViewSet, basename='projects')

urlpatterns = [
    path('', include(router.urls))
]
