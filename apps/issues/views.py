from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from apps.issues.models import IssuesModel
from apps.issues.serializer import IssueSerializer

# Create your views here.


class IssueViewSet(ModelViewSet):
    queryset = IssuesModel.objects.all()
    serializer_class = IssueSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["type", "status", "priority"]
    search_fields = ["title"]
