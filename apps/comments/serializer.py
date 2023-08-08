from apps.comments.models import Comment
from rest_framework import serializers
from apps.users.serializer import UserProfileSerializer
from apps.issues.serializer import IssueSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_by', 'issue', 'created_at', 'updated_at']


class CommentReadOnlySerializer(serializers.ModelSerializer):
    created_by = UserProfileSerializer()
    issue = IssueSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_by', 'issue', 'created_at', 'updated_at', 'is_delete']

    def delete(self, instance):
        instance.is_delete = True
        instance.save()

