from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from apps.issues.models import Issues
from apps.issues.serializer import IssueSerializer, IssueReadOnlySerializer


class IssueViewSet(ModelViewSet):
    queryset = Issues.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["type", "status", "priority"]
    search_fields = ["title"]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return IssueReadOnlySerializer
        return IssueSerializer
