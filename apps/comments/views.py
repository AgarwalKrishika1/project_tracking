from apps.comments.serializer import CommentSerializer, CommentReadOnlySerializer
from rest_framework.viewsets import ModelViewSet
from apps.comments.models import Comment
from rest_framework.permissions import IsAuthenticated


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    allowed_methods = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentReadOnlySerializer
        return CommentSerializer
