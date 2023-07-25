from rest_framework.viewsets import ModelViewSet
from apps.projects.models import Client, Projects, Developer
from apps.projects.serializer import ClientSerializer, ProjectsSerializer, ProjectDeveloperSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.base.permissions import ProjectManagerPermission, SrDeveloperPermission, JrDeveloperPermission
from rest_framework.permissions import IsAuthenticated

class ProjectDeveloperViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = ProjectDeveloperSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


# class IsAuthenticatedOrPostOnly(BasePermission):
#     def has_permission(self, request, view):
#         # Allow any authenticated user to access non-POST requests
#         if request.method != 'POST':
#             return IsAuthenticated().has_permission(request, view)
#         user = request.user
#         if user.is_authenticated and user.userprofile.UserRole == 'project_manager':
#             return True
#
#         return False


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category", "status", "project_manager"]
    search_fields = ["name"]
    allowed_methods = ['get', 'post', 'put', 'patch', 'delete']

    def get_permissions(self):
        permissions = super().get_permissions()
        perm_list = [IsAuthenticated]
        if self.request.method == "PATCH":
            perm_list.append(
                SrDeveloperPermission | ProjectManagerPermission
            )
            return [permission() for permission in perm_list]
        if self.request.method == 'POST':
            return [ProjectManagerPermission()]
        return permissions
