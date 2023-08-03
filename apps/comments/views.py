from apps.comments import CommentSerializer
from rest_framework.viewsets import ModelViewSet
from apps.comments import Comment


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    allowed_methods = ['get', 'post', 'put', 'patch', 'delete']
