from rest_framework.viewsets import ModelViewSet
from apps.projects.models import Client, Projects, Developer
from apps.projects.serializer import ClientSerializer, ProjectsSerializer, ProjectDeveloperSerializer


class ProjectDeveloperViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = ProjectDeveloperSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
