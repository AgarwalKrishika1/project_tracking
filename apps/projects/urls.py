from django.urls import path, include
from apps.projects.views import ClientViewSet, ProjectsViewSet, ProjectDeveloperViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'client', ClientViewSet, basename='clients'),
router.register(r'projects', ProjectsViewSet, basename='projects')
router.register(r'developer', ProjectDeveloperViewSet, basename='developer')

urlpatterns = [
    path('', include(router.urls))
]
