from rest_framework.viewsets import ModelViewSet
from apps.projects.models import Client, Projects, Developer
from apps.projects.serializer import ClientSerializer, ProjectsSerializer, ProjectDeveloperSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.users.models import User

class ProjectDeveloperViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = ProjectDeveloperSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category", "status", "project_manager"]
    search_fields = ["name"]


