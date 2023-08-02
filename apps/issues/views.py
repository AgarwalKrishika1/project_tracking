from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from apps.issues.models import Issues
from apps.issues.serializer import IssueSerializer


class IssueViewSet(ModelViewSet):
    queryset = Issues.objects.all()
    serializer_class = IssueSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["type", "status", "priority"]
    search_fields = ["title"]
