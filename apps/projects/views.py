from rest_framework.viewsets import ModelViewSet
from apps.projects.models import Client, Projects
from apps.projects.serializer import ClientSerializer, ProjectsSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
