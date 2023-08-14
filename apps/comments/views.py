from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from apps.comments.serializer import CommentSerializer, CommentReadOnlySerializer
from rest_framework.viewsets import ModelViewSet
from apps.comments.models import Comment


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["created_by"]
    search_fields = ["text"]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentReadOnlySerializer
        return CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(is_delete=False)
