from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from apps.issues.models import Issue
from apps.issues.serializer import IssueSerializer, IssueReadOnlySerializer
from apps.projects.models import ProjectUser

class IssueViewSet(ModelViewSet):
    queryset = Issue.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["type", "status", "priority"]
    search_fields = ["title"]

    def get_serializer_context(self):
        if self.request.method == "POST":
            if self and not ProjectUser.objects.filter(user=self.request.auth.get('user_id'),
                                                       project=self.request.data.get('projects'),
                                                       isActive=True).exists():
                raise ValueError("Error with user project ")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return IssueReadOnlySerializer
        return IssueSerializer


