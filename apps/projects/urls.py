from django.urls import path, include
from apps.projects.views import ClientViewSet, ProjectViewSet, ProjectDeveloperViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'client', ClientViewSet, basename='clients'),
router.register(r'project', ProjectViewSet, basename='projects')
router.register(r'projectuser', ProjectDeveloperViewSet, basename='projectuser')

urlpatterns = [
    path('', include(router.urls))
]
