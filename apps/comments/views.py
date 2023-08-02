from apps.comments.serializer import CommentSerializer
from rest_framework.viewsets import ModelViewSet
from apps.comments.models import Comment


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    allowed_methods = ['get', 'post', 'put', 'patch', 'delete']
