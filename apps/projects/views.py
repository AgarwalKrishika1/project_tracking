from rest_framework.viewsets import ModelViewSet
from apps.projects.models import Client, Projects, Developer
from apps.projects.serializer import ClientSerializer, ProjectsSerializer, ProjectDeveloperSerializer, \
    ProjectsReadOnlySerialzier
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.base.permissions import ProjectManagerPermission, SrDeveloperPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import CursorPagination


class ProjectDeveloperViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = ProjectDeveloperSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category", "status", "project_manager"]
    search_fields = ["name"]
    allowed_methods = ['get', 'post', 'put', 'patch', 'delete']

    def get_permissions(self):
        perm_list = [IsAuthenticated]
        if self.request.method == "PATCH":
            perm_list.append(
                SrDeveloperPermission | ProjectManagerPermission
            )
        if self.request.method == 'POST':
            perm_list.append(
                ProjectManagerPermission
            )
        return [permission() for permission in perm_list]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProjectsReadOnlySerialzier
        return ProjectsSerializer


class CursorPaginationWithOrder(CursorPagination):
    ordering = 'id'
