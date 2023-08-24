from rest_framework.viewsets import ModelViewSet
from apps.projects.models import Client, Project, ProjectUser
from apps.projects.serializer import ClientSerializer, ProjectSerializer, ProjectUserSerializer, \
    ProjectReadOnlySerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.base.permissions import ProjectManagerPermission, SrDeveloperPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import CursorPagination


class CursorPaginationWithOrder(CursorPagination):
    page_size = 100
    ordering = 'status'


class ProjectDeveloperViewSet(ModelViewSet):
    queryset = ProjectUser.objects.all()
    serializer_class = ProjectUserSerializer

    # def get_serializer_context(self):
    #     if self.request.method == "POST":
    #         if self and not ProjectUser.objects.filter(user=self.request.data.get('user'),
    #                                                    project=self.request.data.get('project')).exists():
    #             raise ValueError("Error with user project ")


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category", "status", "project_manager"]
    search_fields = ["name"]
    pagination_class = CursorPaginationWithOrder

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
            return ProjectReadOnlySerializer
        return ProjectSerializer

    def get_queryset(self):
        query = Project.objects.filter(name__startswith='p')
        return query
