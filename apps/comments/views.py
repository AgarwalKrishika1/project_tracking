from apps.comments.filters import CommentFilterSet
from django_filters.rest_framework import DjangoFilterBackend
from apps.comments.serializer import CommentSerializer, CommentReadOnlySerializer
from rest_framework.viewsets import ModelViewSet
from apps.comments.models import Comment


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.filter(is_delete=False)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["created_by"]
    search_fields = ["text"]
    filterset_class = CommentFilterSet

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentReadOnlySerializer
        return CommentSerializer


